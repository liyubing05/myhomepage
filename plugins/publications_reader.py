"""Plugin: parse BibTeX and expose publications to templates."""

import re
from pathlib import Path

from pelican import signals


def parse_bibtex(filepath):
    """Parse a BibTeX file into a list of publication dicts."""
    text = Path(filepath).read_text(encoding="utf-8")
    entries = []
    pattern = re.compile(
        r'@(\w+)\s*\{\s*(\w+)\s*,\s*(.*?)\}\s*$',
        re.MULTILINE | re.DOTALL,
    )

    def parse_fields(raw):
        fields = {}
        key = None
        depth = 0
        val_start = 0
        i = 0
        while i < len(raw):
            c = raw[i]
            if c == '{':
                if depth == 0 and key is not None:
                    val_start = i + 1
                depth += 1
            elif c == '}':
                depth -= 1
                if depth == 0 and key is not None and val_start > 0:
                    fields[key.lower()] = raw[val_start:i]
                    key = None
            elif c == '"':
                if depth == 0 and key is not None:
                    j = i + 1
                    while j < len(raw) and raw[j] != '"':
                        if raw[j] == '\\':
                            j += 1
                        j += 1
                    fields[key.lower()] = raw[i + 1:j]
                    i = j
            elif depth == 0:
                m = re.match(r'\s*(\w+)\s*=\s*', raw[i:])
                if m:
                    key = m.group(1)
                    i += m.end() - 1
            i += 1
        return fields

    for m in pattern.finditer(text):
        entry_type = m.group(1).lower()
        citekey = m.group(2)
        raw_fields = m.group(3)
        fields = parse_fields(raw_fields)
        fields["_type"] = entry_type
        fields["_key"] = citekey
        entries.append(fields)

    return entries


def format_authors(author_str, highlight_name=None):
    authors = [a.strip() for a in author_str.split(" and ")]
    formatted = []
    for a in authors:
        parts = a.split(",")
        if len(parts) == 2:
            formatted.append(f"{parts[1].strip()} {parts[0].strip()}")
        else:
            formatted.append(a)
        if highlight_name and highlight_name.lower() in a.lower():
            formatted[-1] = f"<strong>{formatted[-1]}</strong>"
    if len(formatted) > 8:
        return ", ".join(formatted[:3]) + ", <em>et al.</em>"
    return ", ".join(formatted)


def inject_publications(pelican_obj):
    """Load publications and inject into Pelican settings as Jinja2 globals."""
    bib_path = pelican_obj.settings.get("BIB_PATH")
    bib_categories = pelican_obj.settings.get("BIB_CATEGORIES") or ()
    author_name = pelican_obj.settings.get("BIB_AUTHOR_NAME") or pelican_obj.settings.get("AUTHOR", "")

    pubs = []
    pub_cats = [label for _, label in bib_categories]

    if bib_path:
        bib_full = Path(bib_path)
        if not bib_full.exists():
            bib_full = Path(pelican_obj.settings.get("PATH", "content")) / bib_path
        if bib_full.exists():
            entries = parse_bibtex(bib_full)
            for e in entries:
                cat = e.get("category", e.get("_type", "article")).lower()
                cat_label = cat.title()
                for key, label in bib_categories:
                    if cat == key:
                        cat_label = label
                        break

                pubs.append({
                    "key": e["_key"],
                    "type": e["_type"],
                    "title": e.get("title", ""),
                    "authors": format_authors(e.get("author", ""), author_name),
                    "author_raw": e.get("author", ""),
                    "journal": e.get("journal", ""),
                    "booktitle": e.get("booktitle", ""),
                    "year": e.get("year", ""),
                    "doi": e.get("doi", ""),
                    "url": e.get("url", ""),
                    "category": cat_label,
                    "abstract": e.get("abstract", ""),
                })

            pubs.sort(key=lambda x: x["year"], reverse=True)

    pelican_obj.settings["PUBLICATIONS"] = pubs
    pelican_obj.settings["PUB_CATEGORIES"] = pub_cats


def register():
    signals.initialized.connect(inject_publications)

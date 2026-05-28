# Yubing Li 李玉冰 — Academic Homepage

Personal academic homepage built with [Pelican](https://getpelican.com). Static site generated from Markdown content and a BibTeX publications file.

## Site Structure

- **Home** — profile, bio, research areas, education, positions, service, projects, contact
- **Publications** — 29 papers (2017–2025) auto-generated from `data/publications.bib` with category filters (Journal / Conference), DOI links, and BibTeX copy-to-clipboard
- **Projects** — self-contained page detailing 5 research directions (USCT, programmable systems, AI-HPC, musculoskeletal imaging, geophysical methods)
- **News** — career milestones, paper acceptances, appointments
- **Team** — graduate recruitment, postdocs, current students, visiting students, alumni

## Quick Start

### Local preview

```
pip install -r requirements.txt
pelican --listen --autoreload -s pelicanconf.py -o output
```

Open http://localhost:8000.

### Adding a publication

Add a BibTeX entry to `data/publications.bib`. Include full author lists and DOIs:

```bibtex
@article{li2026new,
  title     = {Your new paper title},
  author    = {Li, Yubing and Coauthor, First and Coauthor, Second},
  journal   = {Journal Name},
  year      = {2026},
  doi       = {10.xxxx/xxxx},
  category  = {article},
}
```

Rebuild and the publication appears automatically under the correct year heading and category filter. The `publications_reader` plugin parses the BibTeX, formats author lists (with the site author's name highlighted), and generates BibTeX strings for clipboard copy.

### Adding news

Create a Markdown file in `content/news/`:

```markdown
Title: Your News Title
Date: 2026-06-15
Category: news

Your content here.
```

### Editing pages

Edit the Markdown files in `content/pages/`:
- `about.md` — homepage content (bio, research, education, positions, service, projects, contact)
- `projects.md` — detailed project descriptions
- `team.md` — student and recruitment info
- `publications.md` — placeholder (publication list is auto-generated)

### Build for production

```
pelican content -s publishconf.py -o output
```

## Project Structure

```
.
├── pelicanconf.py              # Main config (site name, menus, plugins)
├── publishconf.py              # Production overrides (URL, analytics)
├── requirements.txt            # Python dependencies
├── tasks.py                    # invoke build / serve / deploy commands
│
├── data/
│   └── publications.bib        # BibTeX — single source of truth for publications
│
├── content/
│   ├── images/photo.jpg        # Profile photo
│   ├── pages/                  # Static pages (about, projects, team, publications)
│   └── news/                   # News items (one .md per item)
│
├── plugins/
│   ├── publications_reader.py  # Parses BibTeX, formats authors, generates BibTeX strings
│   └── custom_filters.py       # English date formatting filter
│
├── theme/
│   ├── templates/              # Jinja2 templates
│   └── static/css/style.css    # Stylesheet
│
└── .github/workflows/
    └── deploy.yml              # GitHub Actions: build → deploy to gh-pages
```

## Deployment

Push to `main`. GitHub Actions:

1. Checks out the repo
2. Installs Python dependencies
3. Runs `pelican content -s publishconf.py`
4. Deploys `output/` to GitHub Pages

The site is served from the `gh-pages` branch.

## Theme Customization

Colors and typography are defined as CSS custom properties in `theme/static/css/style.css`:

```css
:root {
    --color-primary: #1a56db;
    --color-bg: #fafbfc;
    --font-sans: ...;
}
```

Edit these to change the site's look without touching any templates.

## License

MIT

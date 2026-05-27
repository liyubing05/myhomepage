# Yubing Li 李玉冰 — Academic Homepage

Personal academic homepage built with [Pelican](https://getpelican.com) and deployed via GitHub Pages. Replaces the previous homepage at [people.ucas.edu.cn/~yubing.li](https://people.ucas.edu.cn/~yubing.li).

## Overview

Static site generated from Markdown content and a BibTeX publications file. Push to `main` and GitHub Actions rebuilds and deploys automatically — no manual steps.

- **Home** — profile photo, bio, research areas, recent news, latest posts
- **Publications** — 29 papers (2017–2025) auto-generated from `data/publications.bib` with category filters (Journal / Conference)
- **CV** — education, positions, professional service, funded projects
- **News** — career milestones, paper acceptances, appointments
- **Teaching** — graduate recruitment, current students, co-supervised students
- **Blog** — research notes and tutorials
- **Projects** — software and research artifacts

## Quick Start

### Local preview

```
pip install -r requirements.txt
pelican --listen --autoreload -s pelicanconf.py -o output
```

Open http://localhost:8000.

### Adding a publication

Add a BibTeX entry to `data/publications.bib`. Use `category = {article}` for journal papers and `category = {inproceedings}` for conference papers.

```bibtex
@article{li2026new,
  title     = {Your new paper title},
  author    = {Li, Yubing and Coauthor, First},
  journal   = {Journal Name},
  year      = {2026},
  category  = {article},
}
```

Push to `main` — the site rebuilds and the publication appears automatically under the correct year heading and category filter.

### Adding news or blog posts

Create a Markdown file in `content/news/` or `content/blog/`:

```markdown
Title: Your Post Title
Date: 2024-06-15
Category: news

Your content here.
```

### Editing pages

Edit the Markdown files in `content/pages/` — About, CV, Teaching are all plain Markdown.

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
│   ├── images/photo.jpg         # Profile photo
│   ├── pages/                   # Static pages (about, cv, teaching, publications)
│   ├── news/                    # News items (one .md per item)
│   ├── blog/                    # Blog posts
│   └── projects/                # Project pages
│
├── plugins/
│   ├── publications_reader.py  # Parses BibTeX and injects data into templates
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

The site is served from the `gh-pages` branch. No manual steps needed.

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

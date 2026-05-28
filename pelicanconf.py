#!/usr/bin/env python
"""Pelican configuration for Yubing Li's academic homepage."""

AUTHOR = "Yubing Li"
SITENAME = "Yubing Li"
SITESUBTITLE = "Institute of Acoustics, Chinese Academy of Sciences"
SITEURL = ""

PATH = "content"
PAGE_PATHS = ["pages"]
ARTICLE_PATHS = ["news"]
STATIC_PATHS = ["images"]

TIMEZONE = "Asia/Shanghai"
DEFAULT_LANG = "en"
LOCALE = "C"

# Date formatting
DATE_FORMATS = {
    "en": "%b %d, %Y",
}
DEFAULT_DATE_FORMAT = "%b %d, %Y"

# URL structure
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"
ARTICLE_URL = "{category}/{slug}/"
ARTICLE_SAVE_AS = "{category}/{slug}/index.html"
CATEGORY_URL = "{slug}/"
CATEGORY_SAVE_AS = "{slug}/index.html"

# Feed generation
FEED_ALL_ATOM = "feeds/all.atom.xml"
FEED_ALL_RSS = "feeds/all.rss.xml"

# Theme
THEME = "theme"

# Plugins
PLUGIN_PATHS = ["plugins"]
PLUGINS = ["publications_reader", "custom_filters"]

# BibTeX publications
BIB_PATH = "data/publications.bib"
BIB_AUTHOR_NAME = "Yubing Li"
BIB_CATEGORIES = (
    ("article", "Journal Papers"),
    ("inproceedings", "Conference Papers"),
)

# Social links
SOCIAL = (
    ("Google Scholar", "https://scholar.google.com/citations?user=9pyKJ50AAAAJ"),
    ("ORCID", "https://orcid.org/0000-0002-6285-2384"),
)

# Navigation menu
MENUITEMS = (
    ("Home", "/"),
    ("Publications", "/publications/"),
    ("Projects", "/projects/"),
    ("News", "/news/"),
    ("Team", "/team/"),
)

DEFAULT_PAGINATION = 10
DEFAULT_DATE = "fs"

# Markdown extensions
MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.extra": {},
        "markdown.extensions.toc": {},
    }
}

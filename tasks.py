"""Invoke tasks for local development."""

from invoke import task


@task
def build(c):
    """Build the site."""
    c.run("pelican content -s pelicanconf.py -o output")


@task
def serve(c):
    """Build and serve locally with auto-reload."""
    c.run("pelican --listen --autoreload -s pelicanconf.py -o output")


@task
def publish(c):
    """Build for production."""
    c.run("pelican content -s publishconf.py -o output")


@task
def deploy(c):
    """Build and deploy to GitHub Pages via ghp-import."""
    c.run("pelican content -s publishconf.py -o output")
    c.run("ghp-import output -m 'Update site' -p")

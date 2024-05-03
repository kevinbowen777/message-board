"""Sphinx configuration."""

project = "message-board"
author = "Kevin Bowen"
copyright = f"2024, {author}"
#
html_theme = "furo"
html_logo = "django_24.png"
html_title = "message-board"
extensions = [
    "sphinx.ext.duration",
]

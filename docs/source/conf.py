import os
import sys

project = "pourewa"
author = "Fraser Callaghan"
copyright = "2026, Fraser Callaghan"

sys.path.insert(0, os.path.abspath("../.."))

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
]

templates_path = ["_templates"]
exclude_patterns = []

html_title = "pourewa documentation"
html_theme = "furo"
html_theme_options = {
    "sidebar_hide_name": False,
    "navigation_with_keys": True,
    "light_css_variables": {
        "color-brand-primary": "#0a7ea4",
        "color-brand-content": "#0a7ea4",
        "font-stack": "Inter, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif",
        "font-stack--monospace": "JetBrains Mono, SFMono-Regular, Menlo, Monaco, Consolas, monospace",
    },
    "dark_css_variables": {
        "color-brand-primary": "#4bb5d6",
        "color-brand-content": "#4bb5d6",
    },
}
html_static_path = ["_static"]
html_css_files = ["custom.css"]

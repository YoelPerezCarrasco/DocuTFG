# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys

sys.path.insert(0, os.path.abspath('.'))

from unittest.mock import MagicMock

class Mock(MagicMock):
    @classmethod
    def __getattr__(cls, name):
        return MagicMock()

# Mock solo de módulos específicos, si es necesario
MOCK_MODULES = ['sqlalchemy','psycopg2']
sys.modules.update((mod_name, Mock()) for mod_name in MOCK_MODULES)


# En conf.py
autodoc_mock_imports = ['sqlalchemy.orm','sqlalchemy.exc','sqlalchemy.ext']


project = 'MyParallelOrg'
copyright = '2024, Yoel Perez Carrasco'
author = 'Yoel Perez Carrasco'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# conf.py

extensions = [
    'myst_parser',
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
]
master_doc = 'index'

myst_enable_extensions = [
    "deflist",
    "colon_fence",
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'es'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import sphinx_rtd_theme

project = 'studt_note'
copyright = '2023, cumeni'
author = 'cumeni'
release = 'V1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

source_suffix = '.rst'


master_doc = 'index'



extensions = []

templates_path = ['_templates']


exclude_patterns = []
# extensions = ['recommonmark','sphinx_markdown_tables']
# extensions = ['recommonmark']


html_sidebars = {
        '**': [
            'about.html',
            'navigation.html',
            'relations.html',
            'searchbox.html',
            'donate.html',
        ]
    }

language = 'zh_CN'



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

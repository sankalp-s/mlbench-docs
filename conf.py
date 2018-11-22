#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# MLBench documentation build configuration file, created by
# sphinx-quickstart on Sun Nov  2 21:31:04 2014.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

#
# Imports
#

import sys
import os

from os.path import abspath, join, dirname

sys.path.insert(0, abspath(join(dirname(__file__))))

# -- RTD configuration ------------------------------------------------

# on_rtd is whether we are on readthedocs.org, this line of code grabbed from docs.readthedocs.org
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

# This is used for linking and such so we link to the thing we're building
rtd_version = os.environ.get('READTHEDOCS_VERSION', 'latest')
if rtd_version not in ['stable', 'latest']:
    rtd_version = 'stable'

# -- General configuration ------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
    'sphinxcontrib.httpdomain',
    'sphinxcontrib.bibtex'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'MLBench'
copyright = '2018 MLBench development team'

# TODO: detect this at
#rtd_version = 'latest'

intersphinx_mapping = {
    'mlbench-helm': ('http://mlbench.readthedocs.io/projects/mlbench_helm/en/%s/' % rtd_version, None),
    'dashboard': ('http://mlbench.readthedocs.io/projects/mlbench_dashboard/en/%s/' % rtd_version, None),
    #'benchmarks': ('http://mlbench.readthedocs.io/projects/mlbench-benchmarks/en/%s/' % rtd_version, None),
    'core': ('http://mlbench.readthedocs.io/projects/mlbench_core/en/%s/' % rtd_version, None),
}

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '2018'
# The full version, including alpha/beta/rc tags.
release = version

autoclass_content = 'both'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'default'

if not on_rtd:  # only import and set the theme if we're building docs locally
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
else:
    html_theme = 'default'

# Output file base name for HTML help builder.
htmlhelp_basename = 'MLBench'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
  ('index', 'MLBench.tex', 'MLBench Documentation',
   'MLBench development team', 'manual'),
]

# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  ('index', 'MLBench', 'MLBench Documentation',
   'MLBench development team', 'MLBench', 'One line description of project.',
   'Miscellaneous'),
]

# -- Options for Epub output ----------------------------------------------

# Bibliographic Dublin Core info.
epub_title = 'MLBench'
epub_author = 'MLBench development team'
epub_publisher = 'MLBench development team'
epub_copyright = '2014-2016, MLBench development team'

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']

# -- Custom Document processing ----------------------------------------------

import gensidebar
gensidebar.generate_sidebar(globals(), 'mlbench')


import sphinx.addnodes
import docutils.nodes

def process_child(node):
    '''This function changes class references to not have the
       intermediate module name by hacking at the doctree'''

    # Edit descriptions to be nicer
    if isinstance(node, sphinx.addnodes.desc_addname):
        if len(node.children) == 1:
            child = node.children[0]
            text = child.astext()

    # Edit literals to be nicer
    elif isinstance(node, docutils.nodes.literal):
        child = node.children[0]
        text = child.astext()

    for child in node.children:
        process_child(child)

def doctree_read(app, doctree):
    for child in doctree.children:
        process_child(child)

def setup(app):
    app.connect('doctree-read', doctree_read)

# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os

# import sys

__abs_file__ = os.path.abspath(__file__)
__repo_docs__ = os.path.dirname(__abs_file__)
__repo_root__ = os.path.dirname(__repo_docs__)
__source_dirs__ = [
    (__repo_root__, "tk-config-default"),
    (__repo_root__, "tk-config-default2"),
]
# sys.path = [os.path.join(*paths) for paths in __source_dirs__] + sys.path


# -- Project information -----------------------------------------------------

project = "rez-shotgun"
author = "Allan Johns, Renaud Lessard Larouche, Brendan Abel, Sebastian Kral, Liam Hoflay, Joseph Yu"
copyright = "2020, {0}".format(author)

# The full version, including alpha/beta/rc tags
release = "0.3.0"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "autoapi.extension",
    "sphinx.ext.napoleon",
    "sphinx_rtd_theme",
]


# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "autoapi/index.rst"]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# -- autoapi.extension --------------------------------------------------------
autoapi_type = "python"
autoapi_dirs = [os.path.join(*paths) for paths in __source_dirs__]

# Helps separate out tk-config-default and tk-config-default2
autoapi_python_use_implicit_namespaces = True

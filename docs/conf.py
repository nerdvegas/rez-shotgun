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


__abs_file__ = os.path.abspath(__file__)
__repo_docs__ = os.path.dirname(__abs_file__)
__repo_root__ = os.path.dirname(__repo_docs__)
__source_dirs__ = [
    (__repo_root__, "tk-config-default"),
    (__repo_root__, "tk-config-default2"),
]


# -- Project information -----------------------------------------------------

__authors__ = (
    "Allan Johns",
    "Renaud Lessard Larouche",
    "Brendan Abel",
    "Sebastian Kral",
    "Liam Hoflay",
    "Joseph Yu",
)
project = "rez-shotgun"
author = ", ".join(__authors__)
copyright = "2020, {0}".format(author)

# The full version, including alpha/beta/rc tags
version = release = "0.3.0"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.githubpages",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    # See doc_requirements.txt
    "autoapi.extension",
    "sphinx_rtd_theme",
    "m2r2",
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


def ensure_static_exists():
    """Make sure ``html_static_path`` exists."""
    for entry in html_static_path:
        static_path = os.path.join(__repo_docs__, entry)
        if not os.path.isdir(static_path):
            os.makedirs(static_path)


ensure_static_exists()
del ensure_static_exists


# A dictionary of values to pass into the template engine’s context for
# all pages. Single values can also be put in this dictionary using the
# -A command-line option of sphinx-build.
html_context = {
    "display_github": True,
    "github_user": "nerdvegas",
    "github_repo": "rez-shotgun",
    "github_version": "master",
    "conf_py_path": "/docs/",
}


# The URL which points to the root of the HTML documentation.
# It is used to indicate the location of document like canonical_url.
html_baseurl = "https://{github_user}.github.io/{github_repo}".format(**html_context)


# -- autoapi.extension --------------------------------------------------------
autoapi_type = "python"
autoapi_dirs = [os.path.join(*_paths) for _paths in __source_dirs__]

# Helps separate out tk-config-default and tk-config-default2
autoapi_python_use_implicit_namespaces = True


# -- sphinx.ext.intersphinx ---------------------------------------------------

intersphinx_mapping = {
    "python": ("https://docs.python.org/2", None),
    "tk-core": ("http://developer.shotgunsoftware.com/tk-core", None),
    "rez": ("https://nerdvegas.github.io/rez/", None),
}

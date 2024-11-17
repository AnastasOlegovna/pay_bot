# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Payment bot'
copyright = '2024, Anastasia Ponomarova'
author = 'Anastasia Ponomarova'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    # 'notfound.extension', #404
    'sphinx_togglebutton',  # dropdown list
    'sphinx_copybutton',  # кнопка скопіювати у тексті з кодом
    'sphinx.ext.autodoc', # може імпортувати модулі, які ви документуєте, і завантажувати документацію з рядків документації напівавтоматично
    # 'sphinx.ext.viewcode',  # додає посилання на виділений вихідний код source in function
    'sphinx.ext.duration',  # звіт про тривалість у кінці виводу консолі
    'sphinx.ext.doctest',  # розширення дозволяє тестувати  фрагменти коду в документації природним способом
    'sphinx.ext.autosummary'  # Створення комплексних посилань на API
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ['_static']

html_favicon = '_static/favicon.ico'

html_last_updated_fmt = '%d %b %Y'
html_show_sourcelink = False
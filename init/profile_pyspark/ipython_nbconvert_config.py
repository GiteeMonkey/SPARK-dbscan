
# Configuration file for ipython-nbconvert.

c = get_config()

#------------------------------------------------------------------------------
# NbConvertApp configuration
#------------------------------------------------------------------------------

# This application is used to convert notebook files (*.ipynb) to various other
# formats.
# 
# WARNING: THE COMMANDLINE INTERFACE MAY CHANGE IN FUTURE RELEASES.

# NbConvertApp will inherit config from: BaseIPythonApplication, Application

# The IPython profile to use.
# c.NbConvertApp.profile = u'default'

# The export format to be used.
# c.NbConvertApp.export_format = 'html'

# Set the log level by value or name.
# c.NbConvertApp.log_level = 30

# List of notebooks to convert. Wildcards are supported. Filenames passed
# positionally will be added to the list.
# c.NbConvertApp.notebooks = []

# Path to an extra config file to load.
# 
# If specified, load this config file in addition to any other IPython config.
# c.NbConvertApp.extra_config_file = u''

# PostProcessor class used to write the  results of the conversion
# c.NbConvertApp.postprocessor_class = u''

# Whether to create profile dir if it doesn't exist
# c.NbConvertApp.auto_create = False

# overwrite base name use for output files. can only  be use when converting one
# notebook at a time.
# c.NbConvertApp.output_base = ''

# The name of the IPython directory. This directory is used for logging
# configuration (through profiles), history storage, etc. The default is usually
# $HOME/.ipython. This options can also be specified through the environment
# variable IPYTHONDIR.
# c.NbConvertApp.ipython_dir = u''

# Whether to install the default config files into the profile dir. If a new
# profile is being created, and IPython contains config files for that profile,
# then they will be staged into the new directory.  Otherwise, default config
# files will be automatically generated.
# c.NbConvertApp.copy_config_files = False

# The date format used by logging formatters for %(asctime)s
# c.NbConvertApp.log_datefmt = '%Y-%m-%d %H:%M:%S'

# The Logging format template
# c.NbConvertApp.log_format = '[%(name)s]%(highlevel)s %(message)s'

# Create a massive crash report when IPython encounters what may be an internal
# error.  The default is to append a short message to the usual traceback
# c.NbConvertApp.verbose_crash = False

# Writer class used to write the  results of the conversion
# c.NbConvertApp.writer_class = 'FilesWriter'

# Whether to overwrite existing config files when copying
# c.NbConvertApp.overwrite = False

#------------------------------------------------------------------------------
# NbConvertBase configuration
#------------------------------------------------------------------------------

# Global configurable class for shared config
# 
# Useful for display data priority that might be use by many transformers

# An ordered list of preferred output type, the first encountered will usually
# be used when converting discarding the others.
# c.NbConvertBase.display_data_priority = ['html', 'application/pdf', 'svg', 'latex', 'png', 'jpg', 'jpeg', 'text']

# default highlight language
# c.NbConvertBase.default_language = 'ipython'

#------------------------------------------------------------------------------
# ProfileDir configuration
#------------------------------------------------------------------------------

# An object to manage the profile directory and its resources.
# 
# The profile directory is used by all IPython applications, to manage
# configuration, logging and security.
# 
# This object knows how to find, create and manage these directories. This
# should be used by any code that wants to handle profiles.

# Set the profile location directly. This overrides the logic used by the
# `profile` option.
# c.ProfileDir.location = u''

#------------------------------------------------------------------------------
# Exporter configuration
#------------------------------------------------------------------------------

# Class containing methods that sequentially run a list of preprocessors on a
# NotebookNode object and then return the modified NotebookNode object and
# accompanying resources dict.

# Extension of the file that should be written to disk
# c.Exporter.file_extension = 'txt'

# List of preprocessors, by name or namespace, to enable.
# c.Exporter.preprocessors = []

# List of preprocessors available by default, by name, namespace,  instance, or
# type.
# c.Exporter.default_preprocessors = ['IPython.nbconvert.preprocessors.coalesce_streams', 'IPython.nbconvert.preprocessors.SVG2PDFPreprocessor', 'IPython.nbconvert.preprocessors.ExtractOutputPreprocessor', 'IPython.nbconvert.preprocessors.CSSHTMLHeaderPreprocessor', 'IPython.nbconvert.preprocessors.RevealHelpPreprocessor', 'IPython.nbconvert.preprocessors.LatexPreprocessor', 'IPython.nbconvert.preprocessors.HighlightMagicsPreprocessor']

#------------------------------------------------------------------------------
# HTMLExporter configuration
#------------------------------------------------------------------------------

# Exports a basic HTML document.  This exporter assists with the export of HTML.
# Inherit from it if you are writing your own HTML template and need custom
# preprocessors/filters.  If you don't need custom preprocessors/ filters, just
# change the 'template_file' config option.

# HTMLExporter will inherit config from: TemplateExporter, Exporter

# 
# c.HTMLExporter.jinja_variable_block_start = ''

# 
# c.HTMLExporter.jinja_variable_block_end = ''

# formats of raw cells to be included in this Exporter's output.
# c.HTMLExporter.raw_mimetypes = []

# Name of the template file to use
# c.HTMLExporter.template_file = u'default'

# List of preprocessors available by default, by name, namespace,  instance, or
# type.
# c.HTMLExporter.default_preprocessors = ['IPython.nbconvert.preprocessors.coalesce_streams', 'IPython.nbconvert.preprocessors.SVG2PDFPreprocessor', 'IPython.nbconvert.preprocessors.ExtractOutputPreprocessor', 'IPython.nbconvert.preprocessors.CSSHTMLHeaderPreprocessor', 'IPython.nbconvert.preprocessors.RevealHelpPreprocessor', 'IPython.nbconvert.preprocessors.LatexPreprocessor', 'IPython.nbconvert.preprocessors.HighlightMagicsPreprocessor']

# 
# c.HTMLExporter.template_path = ['.']

# Extension of the file that should be written to disk
# c.HTMLExporter.file_extension = 'txt'

# 
# c.HTMLExporter.jinja_comment_block_end = ''

# Dictionary of filters, by name and namespace, to add to the Jinja environment.
# c.HTMLExporter.filters = {}

# 
# c.HTMLExporter.jinja_comment_block_start = ''

# 
# c.HTMLExporter.jinja_logic_block_end = ''

# 
# c.HTMLExporter.jinja_logic_block_start = ''

# 
# c.HTMLExporter.template_extension = '.tpl'

# List of preprocessors, by name or namespace, to enable.
# c.HTMLExporter.preprocessors = []

#------------------------------------------------------------------------------
# LatexExporter configuration
#------------------------------------------------------------------------------

# Exports to a Latex template.  Inherit from this class if your template is
# LaTeX based and you need custom tranformers/filters.  Inherit from it if  you
# are writing your own HTML template and need custom tranformers/filters.   If
# you don't need custom tranformers/filters, just change the  'template_file'
# config option.  Place your template in the special "/latex"  subfolder of the
# "../templates" folder.

# LatexExporter will inherit config from: TemplateExporter, Exporter

# 
# c.LatexExporter.jinja_variable_block_start = '((('

# 
# c.LatexExporter.jinja_variable_block_end = ')))'

# formats of raw cells to be included in this Exporter's output.
# c.LatexExporter.raw_mimetypes = []

# Name of the template file to use
# c.LatexExporter.template_file = u'default'

# List of preprocessors available by default, by name, namespace,  instance, or
# type.
# c.LatexExporter.default_preprocessors = ['IPython.nbconvert.preprocessors.coalesce_streams', 'IPython.nbconvert.preprocessors.SVG2PDFPreprocessor', 'IPython.nbconvert.preprocessors.ExtractOutputPreprocessor', 'IPython.nbconvert.preprocessors.CSSHTMLHeaderPreprocessor', 'IPython.nbconvert.preprocessors.RevealHelpPreprocessor', 'IPython.nbconvert.preprocessors.LatexPreprocessor', 'IPython.nbconvert.preprocessors.HighlightMagicsPreprocessor']

# 
# c.LatexExporter.template_path = ['.']

# Extension of the file that should be written to disk
# c.LatexExporter.file_extension = 'txt'

# 
# c.LatexExporter.jinja_comment_block_end = '=))'

# Dictionary of filters, by name and namespace, to add to the Jinja environment.
# c.LatexExporter.filters = {}

# 
# c.LatexExporter.jinja_comment_block_start = '((='

# 
# c.LatexExporter.jinja_logic_block_end = '*))'

# 
# c.LatexExporter.jinja_logic_block_start = '((*'

# 
# c.LatexExporter.template_extension = '.tplx'

# List of preprocessors, by name or namespace, to enable.
# c.LatexExporter.preprocessors = []

#------------------------------------------------------------------------------
# MarkdownExporter configuration
#------------------------------------------------------------------------------

# Exports to a markdown document (.md)

# MarkdownExporter will inherit config from: TemplateExporter, Exporter

# 
# c.MarkdownExporter.jinja_variable_block_start = ''

# 
# c.MarkdownExporter.jinja_variable_block_end = ''

# formats of raw cells to be included in this Exporter's output.
# c.MarkdownExporter.raw_mimetypes = []

# Name of the template file to use
# c.MarkdownExporter.template_file = u'default'

# List of preprocessors available by default, by name, namespace,  instance, or
# type.
# c.MarkdownExporter.default_preprocessors = ['IPython.nbconvert.preprocessors.coalesce_streams', 'IPython.nbconvert.preprocessors.SVG2PDFPreprocessor', 'IPython.nbconvert.preprocessors.ExtractOutputPreprocessor', 'IPython.nbconvert.preprocessors.CSSHTMLHeaderPreprocessor', 'IPython.nbconvert.preprocessors.RevealHelpPreprocessor', 'IPython.nbconvert.preprocessors.LatexPreprocessor', 'IPython.nbconvert.preprocessors.HighlightMagicsPreprocessor']

# 
# c.MarkdownExporter.template_path = ['.']

# Extension of the file that should be written to disk
# c.MarkdownExporter.file_extension = 'txt'

# 
# c.MarkdownExporter.jinja_comment_block_end = ''

# Dictionary of filters, by name and namespace, to add to the Jinja environment.
# c.MarkdownExporter.filters = {}

# 
# c.MarkdownExporter.jinja_comment_block_start = ''

# 
# c.MarkdownExporter.jinja_logic_block_end = ''

# 
# c.MarkdownExporter.jinja_logic_block_start = ''

# 
# c.MarkdownExporter.template_extension = '.tpl'

# List of preprocessors, by name or namespace, to enable.
# c.MarkdownExporter.preprocessors = []

#------------------------------------------------------------------------------
# PythonExporter configuration
#------------------------------------------------------------------------------

# Exports a Python code file.

# PythonExporter will inherit config from: TemplateExporter, Exporter

# 
# c.PythonExporter.jinja_variable_block_start = ''

# 
# c.PythonExporter.jinja_variable_block_end = ''

# formats of raw cells to be included in this Exporter's output.
# c.PythonExporter.raw_mimetypes = []

# Name of the template file to use
# c.PythonExporter.template_file = u'default'

# List of preprocessors available by default, by name, namespace,  instance, or
# type.
# c.PythonExporter.default_preprocessors = ['IPython.nbconvert.preprocessors.coalesce_streams', 'IPython.nbconvert.preprocessors.SVG2PDFPreprocessor', 'IPython.nbconvert.preprocessors.ExtractOutputPreprocessor', 'IPython.nbconvert.preprocessors.CSSHTMLHeaderPreprocessor', 'IPython.nbconvert.preprocessors.RevealHelpPreprocessor', 'IPython.nbconvert.preprocessors.LatexPreprocessor', 'IPython.nbconvert.preprocessors.HighlightMagicsPreprocessor']

# 
# c.PythonExporter.template_path = ['.']

# Extension of the file that should be written to disk
# c.PythonExporter.file_extension = 'txt'

# 
# c.PythonExporter.jinja_comment_block_end = ''

# Dictionary of filters, by name and namespace, to add to the Jinja environment.
# c.PythonExporter.filters = {}

# 
# c.PythonExporter.jinja_comment_block_start = ''

# 
# c.PythonExporter.jinja_logic_block_end = ''

# 
# c.PythonExporter.jinja_logic_block_start = ''

# 
# c.PythonExporter.template_extension = '.tpl'

# List of preprocessors, by name or namespace, to enable.
# c.PythonExporter.preprocessors = []

#------------------------------------------------------------------------------
# RSTExporter configuration
#------------------------------------------------------------------------------

# Exports restructured text documents.

# RSTExporter will inherit config from: TemplateExporter, Exporter

# 
# c.RSTExporter.jinja_variable_block_start = ''

# 
# c.RSTExporter.jinja_variable_block_end = ''

# formats of raw cells to be included in this Exporter's output.
# c.RSTExporter.raw_mimetypes = []

# Name of the template file to use
# c.RSTExporter.template_file = u'default'

# List of preprocessors available by default, by name, namespace,  instance, or
# type.
# c.RSTExporter.default_preprocessors = ['IPython.nbconvert.preprocessors.coalesce_streams', 'IPython.nbconvert.preprocessors.SVG2PDFPreprocessor', 'IPython.nbconvert.preprocessors.ExtractOutputPreprocessor', 'IPython.nbconvert.preprocessors.CSSHTMLHeaderPreprocessor', 'IPython.nbconvert.preprocessors.RevealHelpPreprocessor', 'IPython.nbconvert.preprocessors.LatexPreprocessor', 'IPython.nbconvert.preprocessors.HighlightMagicsPreprocessor']

# 
# c.RSTExporter.template_path = ['.']

# Extension of the file that should be written to disk
# c.RSTExporter.file_extension = 'txt'

# 
# c.RSTExporter.jinja_comment_block_end = ''

# Dictionary of filters, by name and namespace, to add to the Jinja environment.
# c.RSTExporter.filters = {}

# 
# c.RSTExporter.jinja_comment_block_start = ''

# 
# c.RSTExporter.jinja_logic_block_end = ''

# 
# c.RSTExporter.jinja_logic_block_start = ''

# 
# c.RSTExporter.template_extension = '.tpl'

# List of preprocessors, by name or namespace, to enable.
# c.RSTExporter.preprocessors = []

#------------------------------------------------------------------------------
# SlidesExporter configuration
#------------------------------------------------------------------------------

# Exports HTML slides with reveal.js

# SlidesExporter will inherit config from: HTMLExporter, TemplateExporter,
# Exporter

# 
# c.SlidesExporter.jinja_variable_block_start = ''

# 
# c.SlidesExporter.jinja_variable_block_end = ''

# formats of raw cells to be included in this Exporter's output.
# c.SlidesExporter.raw_mimetypes = []

# Name of the template file to use
# c.SlidesExporter.template_file = u'default'

# List of preprocessors available by default, by name, namespace,  instance, or
# type.
# c.SlidesExporter.default_preprocessors = ['IPython.nbconvert.preprocessors.coalesce_streams', 'IPython.nbconvert.preprocessors.SVG2PDFPreprocessor', 'IPython.nbconvert.preprocessors.ExtractOutputPreprocessor', 'IPython.nbconvert.preprocessors.CSSHTMLHeaderPreprocessor', 'IPython.nbconvert.preprocessors.RevealHelpPreprocessor', 'IPython.nbconvert.preprocessors.LatexPreprocessor', 'IPython.nbconvert.preprocessors.HighlightMagicsPreprocessor']

# 
# c.SlidesExporter.template_path = ['.']

# Extension of the file that should be written to disk
# c.SlidesExporter.file_extension = 'txt'

# 
# c.SlidesExporter.jinja_comment_block_end = ''

# Dictionary of filters, by name and namespace, to add to the Jinja environment.
# c.SlidesExporter.filters = {}

# 
# c.SlidesExporter.jinja_comment_block_start = ''

# 
# c.SlidesExporter.jinja_logic_block_end = ''

# 
# c.SlidesExporter.jinja_logic_block_start = ''

# 
# c.SlidesExporter.template_extension = '.tpl'

# List of preprocessors, by name or namespace, to enable.
# c.SlidesExporter.preprocessors = []

#------------------------------------------------------------------------------
# TemplateExporter configuration
#------------------------------------------------------------------------------

# Exports notebooks into other file formats.  Uses Jinja 2 templating engine to
# output new formats.  Inherit from this class if you are creating a new
# template type along with new filters/preprocessors.  If the filters/
# preprocessors provided by default suffice, there is no need to inherit from
# this class.  Instead, override the template_file and file_extension traits via
# a config file.
# 
# - citation2latex - highlight2html - filter_data_type - markdown2html -
# markdown2rst - get_lines - ansi2latex - strip_ansi - add_prompts -
# comment_lines - ascii_only - markdown2latex - escape_latex - add_anchor -
# ipython2python - posix_path - highlight2latex - path2url - ansi2html -
# wrap_text - indent - strip_dollars - html2text - strip_files_prefix

# TemplateExporter will inherit config from: Exporter

# 
# c.TemplateExporter.jinja_variable_block_start = ''

# 
# c.TemplateExporter.jinja_variable_block_end = ''

# formats of raw cells to be included in this Exporter's output.
# c.TemplateExporter.raw_mimetypes = []

# Name of the template file to use
# c.TemplateExporter.template_file = u'default'

# List of preprocessors available by default, by name, namespace,  instance, or
# type.
# c.TemplateExporter.default_preprocessors = ['IPython.nbconvert.preprocessors.coalesce_streams', 'IPython.nbconvert.preprocessors.SVG2PDFPreprocessor', 'IPython.nbconvert.preprocessors.ExtractOutputPreprocessor', 'IPython.nbconvert.preprocessors.CSSHTMLHeaderPreprocessor', 'IPython.nbconvert.preprocessors.RevealHelpPreprocessor', 'IPython.nbconvert.preprocessors.LatexPreprocessor', 'IPython.nbconvert.preprocessors.HighlightMagicsPreprocessor']

# 
# c.TemplateExporter.template_path = ['.']

# Extension of the file that should be written to disk
# c.TemplateExporter.file_extension = 'txt'

# 
# c.TemplateExporter.jinja_comment_block_end = ''

# Dictionary of filters, by name and namespace, to add to the Jinja environment.
# c.TemplateExporter.filters = {}

# 
# c.TemplateExporter.jinja_comment_block_start = ''

# 
# c.TemplateExporter.jinja_logic_block_end = ''

# 
# c.TemplateExporter.jinja_logic_block_start = ''

# 
# c.TemplateExporter.template_extension = '.tpl'

# List of preprocessors, by name or namespace, to enable.
# c.TemplateExporter.preprocessors = []

#------------------------------------------------------------------------------
# CSSHTMLHeaderPreprocessor configuration
#------------------------------------------------------------------------------

# Preprocessor used to pre-process notebook for HTML output.  Adds IPython
# notebook front-end CSS and Pygments CSS to HTML output.

# CSSHTMLHeaderPreprocessor will inherit config from: Preprocessor,
# NbConvertBase

# default highlight language
# c.CSSHTMLHeaderPreprocessor.default_language = 'ipython'

# CSS highlight class identifier
# c.CSSHTMLHeaderPreprocessor.highlight_class = '.highlight'


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
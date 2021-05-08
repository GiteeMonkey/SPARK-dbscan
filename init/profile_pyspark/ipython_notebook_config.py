
# Configuration file for ipython-notebook.

c = get_config()

c.NotebookApp.ip = '*'
c.NotebookApp.open_browser = False
c.NotebookApp.port = 8889

#------------------------------------------------------------------------------
# NotebookApp configuration
#------------------------------------------------------------------------------

# NotebookApp will inherit config from: BaseIPythonApplication, Application

# The url for MathJax.js.
# c.NotebookApp.mathjax_url = ''

# Supply extra arguments that will be passed to Jinja environment.
# c.NotebookApp.jinja_environment_options = {}

# The IP address the notebook server will listen on.
# c.NotebookApp.ip = 'localhost'

# DEPRECATED use base_url
# c.NotebookApp.base_project_url = '/'

# Create a massive crash report when IPython encounters what may be an internal
# error.  The default is to append a short message to the usual traceback
# c.NotebookApp.verbose_crash = False

# The random bytes used to secure cookies. By default this is a new random
# number every time you start the Notebook. Set it to a value in a config file
# to enable logins to persist across server sessions.
#
# Note: Cookie secrets should be kept private, do not share config files with
# cookie_secret stored in plaintext (you can read the value from a file).
# c.NotebookApp.cookie_secret = ''

# The number of additional ports to try if the specified port is not available.
# c.NotebookApp.port_retries = 50

# Whether to open in a browser after starting. The specific browser used is
# platform dependent and determined by the python standard library `webbrowser`
# module, unless it is overridden using the --browser (NotebookApp.browser)
# configuration option.
# c.NotebookApp.open_browser = True

# The notebook manager class to use.
# c.NotebookApp.notebook_manager_class = 'IPython.html.services.notebooks.filenbmanager.FileNotebookManager'

# The date format used by logging formatters for %(asctime)s
# c.NotebookApp.log_datefmt = '%Y-%m-%d %H:%M:%S'

# The port the notebook server will listen on.
# c.NotebookApp.port = 8888

# Whether to overwrite existing config files when copying
# c.NotebookApp.overwrite = False

# Set the Access-Control-Allow-Origin header
#
# Use '*' to allow any origin to access your server.
#
# Takes precedence over allow_origin_pat.
# c.NotebookApp.allow_origin = ''

# Whether to enable MathJax for typesetting math/TeX
#
# MathJax is the javascript library IPython uses to render math/LaTeX. It is
# very large, so you may want to disable it if you have a slow internet
# connection, or for offline use of the notebook.
#
# When disabled, equations etc. will appear as their untransformed TeX source.
# c.NotebookApp.enable_mathjax = True

# Use a regular expression for the Access-Control-Allow-Origin header
#
# Requests from an origin matching the expression will get replies with:
#
#     Access-Control-Allow-Origin: origin
#
# where `origin` is the origin of the request.
#
# Ignored if allow_origin is set.
# c.NotebookApp.allow_origin_pat = ''

# The full path to an SSL/TLS certificate file.
# c.NotebookApp.certfile = u''

# The base URL for the notebook server.
#
# Leading and trailing slashes can be omitted, and will automatically be added.
# c.NotebookApp.base_url = '/'

# The directory to use for notebooks and kernels.
# c.NotebookApp.notebook_dir = u'/Users/dmartin/Desktop/Dev/Vectorworks/Engineering/Nebula/Mainline/Servers/analytics/ipython-data-notebooks'

#
# c.NotebookApp.file_to_run = ''

# The IPython profile to use.
# c.NotebookApp.profile = u'default'

# paths for Javascript extensions. By default, this is just
# IPYTHONDIR/nbextensions
# c.NotebookApp.nbextensions_path = []

# The Logging format template
# c.NotebookApp.log_format = '[%(name)s]%(highlevel)s %(message)s'

# The name of the IPython directory. This directory is used for logging
# configuration (through profiles), history storage, etc. The default is usually
# $HOME/.ipython. This options can also be specified through the environment
# variable IPYTHONDIR.
# c.NotebookApp.ipython_dir = u''

# Set the log level by value or name.
# c.NotebookApp.log_level = 30

# Hashed password to use for web authentication.
#
# To generate, type in a python/IPython shell:
#
#   from IPython.lib import passwd; passwd()
#
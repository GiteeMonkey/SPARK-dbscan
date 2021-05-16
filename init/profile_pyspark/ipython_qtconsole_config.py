
# Configuration file for ipython-qtconsole.

c = get_config()

#------------------------------------------------------------------------------
# IPythonQtConsoleApp configuration
#------------------------------------------------------------------------------

# IPythonQtConsoleApp will inherit config from: BaseIPythonApplication,
# Application, IPythonConsoleApp, ConnectionFileMixin

# Set the kernel's IP address [default localhost]. If the IP address is
# something other than localhost, then Consoles on other machines will be able
# to connect to the Kernel, so be careful!
# c.IPythonQtConsoleApp.ip = u''

# Create a massive crash report when IPython encounters what may be an internal
# error.  The default is to append a short message to the usual traceback
# c.IPythonQtConsoleApp.verbose_crash = False

# Start the console window maximized.
# c.IPythonQtConsoleApp.maximize = False

# The date format used by logging formatters for %(asctime)s
# c.IPythonQtConsoleApp.log_datefmt = '%Y-%m-%d %H:%M:%S'

# set the shell (ROUTER) port [default: random]
# c.IPythonQtConsoleApp.shell_port = 0

# The SSH server to use to connect to the kernel.
# c.IPythonQtConsoleApp.sshserver = ''

# set the stdin (DEALER) port [default: random]
# c.IPythonQtConsoleApp.stdin_port = 0

# Set the log level by value or name.
# c.IPythonQtConsoleApp.log_level = 30

# Path to the ssh key to use for logging in to the ssh server.
# c.IPythonQtConsoleApp.sshkey = ''

# Path to an extra config file to load.
# 
# If specified, load this config file in addition to any other IPython config.
# c.IPythonQtConsoleApp.extra_config_file = u''

# Whether to create profile dir if it doesn't exist
# c.IPythonQtConsoleApp.auto_create = False

# path to a custom CSS stylesheet
# c.IPythonQtConsoleApp.stylesheet = ''

# set the heartbeat port [default: random]
# c.IPythonQtConsoleApp.hb_port = 0

# Whether to overwrite existing config files when copying
# c.IPythonQtConsoleApp.overwrite = False

# set the iopub (PUB) port [default: random]
# c.IPythonQtConsoleApp.iopub_port = 0

# The IPython profile to use.
# c.IPythonQtConsoleApp.profile = u'default'

# JSON file in which to store connection info [default: kernel-<pid>.json]
# 
# This file will contain the IP, ports, and authentication key needed to connect
# clients to this kernel. By default, this file will be created in the security-
# dir of the current profile, but can be specified by absolute path.
# c.IPythonQtConsoleApp.connection_file = ''

# Set to display confirmation dialog on exit. You can always use 'exit' or
# 'quit', to force a direct exit without any confirmation.
# c.IPythonQtConsoleApp.confirm_exit = True

# The name of the IPython directory. This directory is used for logging
# configuration (through profiles), history storage, etc. The default is usually
# $HOME/.ipython. This options can also be specified through the environment
# variable IPYTHONDIR.
# c.IPythonQtConsoleApp.ipython_dir = u''

# Whether to install the default config files into the profile dir. If a new
# profile is being created, and IPython contains config files for that profile,
# then they will be staged into the new directory.  Otherwise, default config
# files will be automatically generated.
# c.IPythonQtConsoleApp.copy_config_files = False

# Connect to an already running kernel
# c.IPythonQtConsoleApp.existing = ''

# Use a plaintext widget instead of rich text (plain can't print/save).
# c.IPythonQtConsoleApp.plain = False

# Start the console window with the menu bar hidden.
# c.IPythonQtConsoleApp.hide_menubar = False

# The Logging format template
# c.IPythonQtConsoleApp.log_format = '[%(name)s]%(highlevel)s %(message)s'

# 
# c.IPythonQtConsoleApp.transport = 'tcp'

#------------------------------------------------------------------------------
# IPythonWidget configuration
#------------------------------------------------------------------------------

# A FrontendWidget for an IPython kernel.

# IPythonWidget will inherit config from: FrontendWidget, HistoryConsoleWidget,
# ConsoleWidget

# The type of completer to use. Valid values are:
# 
# 'plain'   : Show the available completion as a text list
#             Below the editing area.
# 'droplist': Show the completion in a drop down list navigable
#             by the arrow keys, and from which you can select
#             completion by pressing Return.
# 'ncurses' : Show the completion as a text list which is navigable by
#             `tab` and arrow keys.
# c.IPythonWidget.gui_completion = 'ncurses'

# Whether to process ANSI escape codes.
# c.IPythonWidget.ansi_codes = True

# A CSS stylesheet. The stylesheet can contain classes for:
#     1. Qt: QPlainTextEdit, QFrame, QWidget, etc
#     2. Pygments: .c, .k, .o, etc. (see PygmentsHighlighter)
#     3. IPython: .error, .in-prompt, .out-prompt, etc
# c.IPythonWidget.style_sheet = u''

# The height of the console at start time in number of characters (will double
# with `vsplit` paging)
# c.IPythonWidget.height = 25

# 
# c.IPythonWidget.out_prompt = 'Out[<span class="out-prompt-number">%i</span>]: '

# 
# c.IPythonWidget.input_sep = '\n'

# Whether to draw information calltips on open-parentheses.
# c.IPythonWidget.enable_calltips = True

# 
# c.IPythonWidget.in_prompt = 'In [<span class="in-prompt-number">%i</span>]: '

# The width of the console at start time in number of characters (will double
# with `hsplit` paging)
# c.IPythonWidget.width = 81

# A command for invoking a system text editor. If the string contains a
# {filename} format specifier, it will be used. Otherwise, the filename will be
# appended to the end the command.
# c.IPythonWidget.editor = ''

# If not empty, use this Pygments style for syntax highlighting. Otherwise, the
# style sheet is queried for Pygments style information.
# c.IPythonWidget.syntax_style = u''

# The font family to use for the console. On OSX this defaults to Monaco, on
# Windows the default is Consolas with fallback of Courier, and on other
# platforms the default is Monospace.
# c.IPythonWidget.font_family = u''

# The pygments lexer class to use.
# c.IPythonWidget.lexer_class = <IPython.utils.traitlets.Undefined object at 0x10258ded0>

# 
# c.IPythonWidget.output_sep2 = ''

# Whether to automatically execute on syntactically complete input.
# 
# If False, Shift-Enter is required to submit each execution. Disabling this is
# mainly useful for non-Python kernels, where the completion check would be
# wrong.
# c.IPythonWidget.execute_on_complete_input = True

# The maximum number of lines of text before truncation. Specifying a non-
# positive number disables text truncation (not recommended).
# c.IPythonWidget.buffer_size = 500

# 
# c.IPythonWidget.history_lock = False

# 
# c.IPythonWidget.banner = u''

# The type of underlying text widget to use. Valid values are 'plain', which
# specifies a QPlainTextEdit, and 'rich', which specifies a QTextEdit.
# c.IPythonWidget.kind = 'plain'

# Whether to ask for user confirmation when restarting kernel
# c.IPythonWidget.confirm_restart = True

# The font size. If unconfigured, Qt will be entrusted with the size of the
# font.
# c.IPythonWidget.font_size = 0

# The editor command to use when a specific line number is requested. The string
# should contain two format specifiers: {line} and {filename}. If this parameter
# is not specified, the line number option to the %edit magic will be ignored.
# c.IPythonWidget.editor_line = u''

# Whether to clear the console when the kernel is restarted
# c.IPythonWidget.clear_on_kernel_restart = True

# The type of paging to use. Valid values are:
# 
# 'inside'
#    The widget pages like a traditional terminal.
# 'hsplit'
#    When paging is requested, the widget is split horizontally. The top
#    pane contains the console, and the bottom pane contains the paged text.
# 'vsplit'
#    Similar to 'hsplit', except that a vertical splitter is used.
# 'custom'
#    No action is taken by the widget beyond emitting a
#    'custom_page_requested(str)' signal.
# 'none'
#    The text is written directly to the console.
# c.IPythonWidget.paging = 'inside'

# 
# c.IPythonWidget.output_sep = ''

#------------------------------------------------------------------------------
# IPKernelApp configuration
#------------------------------------------------------------------------------

# IPython: an enhanced interactive Python shell.

# IPKernelApp will inherit config from: BaseIPythonApplication, Application,
# InteractiveShellApp

# Run the file referenced by the PYTHONSTARTUP environment variable at IPython
# startup.
# c.IPKernelApp.exec_PYTHONSTARTUP = True

# The importstring for the DisplayHook factory
# c.IPKernelApp.displayhook_class = 'IPython.kernel.zmq.displayhook.ZMQDisplayHook'

# Set the IP or interface on which the kernel will listen.
# c.IPKernelApp.ip = u''

# Pre-load matplotlib and numpy for interactive use, selecting a particular
# matplotlib backend and loop integration.
# c.IPKernelApp.pylab = None

# Create a massive crash report when IPython encounters what may be an internal
# error.  The default is to append a short message to the usual traceback
# c.IPKernelApp.verbose_crash = False

# The Kernel subclass to be used.
# 
# This should allow easy re-use of the IPKernelApp entry point to configure and
# launch kernels other than IPython's own.
# c.IPKernelApp.kernel_class = 'IPython.kernel.zmq.ipkernel.Kernel'

# Run the module as a script.
# c.IPKernelApp.module_to_run = ''

# The date format used by logging formatters for %(asctime)s
# c.IPKernelApp.log_datefmt = '%Y-%m-%d %H:%M:%S'

# set the shell (ROUTER) port [default: random]
# c.IPKernelApp.shell_port = 0

# set the control (ROUTER) port [default: random]
# c.IPKernelApp.control_port = 0

# Whether to overwrite existing config files when copying
# c.IPKernelApp.overwrite = False

# Execute the given command string.
# c.IPKernelApp.code_to_run = ''

# set the stdin (ROUTER) port [default: random]
# c.IPKernelApp.stdin_port = 0

# Set the log level by value or name.
# c.IPKernelApp.log_level = 30

# lines of code to run at IPython startup.
# c.IPKernelApp.exec_lines = []

# Path to an extra config file to load.
# 
# If specified, load this config file in addition to any other IPython config.
# c.IPKernelApp.extra_config_file = u''

# The importstring for the OutStream factory
# c.IPKernelApp.outstream_class = 'IPython.kernel.zmq.iostream.OutStream'

# Whether to create profile dir if it doesn't exist
# c.IPKernelApp.auto_create = False

# set the heartbeat port [default: random]
# c.IPKernelApp.hb_port = 0

# 
# c.IPKernelApp.transport = 'tcp'

# redirect stdout to the null device
# c.IPKernelApp.no_stdout = False

# Should variables loaded at startup (by startup files, exec_lines, etc.) be
# hidden from tools like %who?
# c.IPKernelApp.hide_initial_ns = True

# dotted module name of an IPython extension to load.
# c.IPKernelApp.extra_extension = ''

# A file to be run
# c.IPKernelApp.file_to_run = ''

# The IPython profile to use.
# c.IPKernelApp.profile = u'default'

# 
# c.IPKernelApp.parent_appname = u''

# kill this process if its parent dies.  On Windows, the argument specifies the
# HANDLE of the parent process, otherwise it is simply boolean.
# c.IPKernelApp.parent_handle = 0

# JSON file in which to store connection info [default: kernel-<pid>.json]
# 
# This file will contain the IP, ports, and authentication key needed to connect
# clients to this kernel. By default, this file will be created in the security
# dir of the current profile, but can be specified by absolute path.
# c.IPKernelApp.connection_file = ''

# If true, IPython will populate the user namespace with numpy, pylab, etc. and
# an ``import *`` is done from numpy and pylab, when using pylab mode.
# 
# When False, pylab mode should not import any names into the user namespace.
# c.IPKernelApp.pylab_import_all = True

# The name of the IPython directory. This directory is used for logging
# configuration (through profiles), history storage, etc. The default is usually
# $HOME/.ipython. This options can also be specified through the environment
# variable IPYTHONDIR.
# c.IPKernelApp.ipython_dir = u''

# Configure matplotlib for interactive use with the default matplotlib backend.
# c.IPKernelApp.matplotlib = None

# ONLY USED ON WINDOWS Interrupt this process when the parent is signaled.
# c.IPKernelApp.interrupt = 0

# Whether to install the default config files into the profile dir. If a new
# profile is being created, and IPython contains config files for that profile,
# then they will be staged into the new directory.  Otherwise, default config
# files will be automatically generated.
# c.IPKernelApp.copy_config_files = False

# List of files to run at IPython startup.
# c.IPKernelApp.exec_files = []

# Enable GUI event loop integration with any of ('glut', 'gtk', 'gtk3', 'none',
# 'osx', 'pyglet', 'qt', 'qt4', 'tk', 'wx').
# c.IPKernelApp.gui = None

# A list of dotted module names of IPython extensions to load.
# c.IPKernelApp.extensions = []

# redirect stderr to the null device
# c.IPKernelApp.no_stderr = False

# The Logging format template
# c.IPKernelApp.log_format = '[%(name)s]%(highlevel)s %(message)s'

# set the iopub (PUB) port [default: random]
# c.IPKernelApp.iopub_port = 0

#------------------------------------------------------------------------------
# ZMQInteractiveShell configuration
#------------------------------------------------------------------------------

# A subclass of InteractiveShell for ZMQ.

# ZMQInteractiveShell will inherit config from: InteractiveShell

# Use colors for displaying information about objects. Because this information
# is passed through a pager (like 'less'), and some pagers get confused with
# color codes, this capability can be turned off.
# c.ZMQInteractiveShell.color_info = True

# A list of ast.NodeTransformer subclass instances, which will be applied to
# user input before code is run.
# c.ZMQInteractiveShell.ast_transformers = []

# 
# c.ZMQInteractiveShell.history_length = 10000

# Don't call post-execute functions that have failed in the past.
# c.ZMQInteractiveShell.disable_failing_post_execute = False

# Show rewritten input, e.g. for autocall.
# c.ZMQInteractiveShell.show_rewritten_input = True

# Set the color scheme (NoColor, Linux, or LightBG).
# c.ZMQInteractiveShell.colors = 'LightBG'

# 
# c.ZMQInteractiveShell.separate_in = '\n'

# Deprecated, use PromptManager.in2_template
# c.ZMQInteractiveShell.prompt_in2 = '   .\\D.: '

# 
# c.ZMQInteractiveShell.separate_out = ''

# Deprecated, use PromptManager.in_template
# c.ZMQInteractiveShell.prompt_in1 = 'In [\\#]: '

# Enable deep (recursive) reloading by default. IPython can use the deep_reload
# module which reloads changes in modules recursively (it replaces the reload()
# function, so you don't need to change anything to use it). deep_reload()
# forces a full reload of modules whose code may have changed, which the default
# reload() function does not.  When deep_reload is off, IPython will use the
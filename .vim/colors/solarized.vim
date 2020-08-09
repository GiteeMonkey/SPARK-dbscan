
" Name:     Solarized vim colorscheme
" Author:   Ethan Schoonover <es@ethanschoonover.com>
" URL:      http://ethanschoonover.com/solarized
"           (see this url for latest release & screenshots)
" License:  OSI approved MIT license (see end of this file)
" Created:  In the middle of the night
" Modified: 2011 Apr 14
"
" Usage "{{{
"
" ---------------------------------------------------------------------
" ABOUT:
" ---------------------------------------------------------------------
" Solarized is a carefully designed selective contrast colorscheme with dual
" light and dark modes that runs in both GUI, 256 and 16 color modes.
"
" See the homepage above for screenshots and details.
"
" ---------------------------------------------------------------------
" INSTALLATION:
" ---------------------------------------------------------------------
"
" Two options for installation: manual or pathogen
"
" MANUAL INSTALLATION OPTION:
" ---------------------------------------------------------------------
"
" 1.  Put the files in the right place!
" 2.  Move `solarized.vim` to your `.vim/colors` directory.
"
" RECOMMENDED PATHOGEN INSTALLATION OPTION:
" ---------------------------------------------------------------------
"
" 1.  Download and install Tim Pope's Pathogen from:
"     https://github.com/tpope/vim-pathogen
"
" 2.  Next, move or clone the `vim-colors-solarized` directory so that it is
"     a subdirectory of the `.vim/bundle` directory.
"
"     a. **clone with git:**
"
"       $ cd ~/.vim/bundle
"       $ git clone git://github.com/altercation/vim-colors-solarized.git
"
"     b. **or move manually into the pathogen bundle directory:**
"         In the parent directory of vim-colors-solarized:
"
"         $ mv vim-colors-solarized ~/.vim/bundle/
"
" MODIFY VIMRC:
"
" After either Option 1 or Option 2 above, put the following two lines in your
" .vimrc:
"
"     syntax enable
"     set background=dark
"     colorscheme solarized
"
" or, for the light background mode of Solarized:
"
"     syntax enable
"     set background=light
"     colorscheme solarized
"
" I like to have a different background in GUI and terminal modes, so I can use
" the following if-then. However, I find vim's background autodetection to be
" pretty good and, at least with MacVim, I can leave this background value
" assignment out entirely and get the same results.
"
"     if has('gui_running')
"       set background=light
"     else
"       set background=dark
"     endif
"
" See the Solarized homepage at http://ethanschoonover.com/solarized for
" screenshots which will help you select either the light or dark background.
"
" Other options are detailed below.
"
" IMPORTANT NOTE FOR TERMINAL USERS:
"
" If you are going to use Solarized in Terminal mode (i.e. not in a GUI version
" like gvim or macvim), **please please please** consider setting your terminal
" emulator's colorscheme to used the Solarized palette. I've included palettes
" for some popular terminal emulator as well as Xdefaults in the official
" Solarized download available from [Solarized homepage]. If you use
" Solarized *without* these colors, Solarized will need to be told to degrade
" its colorscheme to a set compatible with the limited 256 terminal palette
" (whereas by using the terminal's 16 ansi color values, you can set the
" correct, specific values for the Solarized palette).
"
" If you do use the custom terminal colors, solarized.vim should work out of
" the box for you. If you are using a terminal emulator that supports 256
" colors and don't want to use the custom Solarized terminal colors, you will
" need to use the degraded 256 colorscheme. To do so, simply add the following
" line *before* the `colorschem solarized` line:
"
"     let g:solarized_termcolors=256
"
" Again, I recommend just changing your terminal colors to Solarized values
" either manually or via one of the many terminal schemes available for import.
"
" ---------------------------------------------------------------------
" TOGGLE BACKGROUND FUNCTION:
" ---------------------------------------------------------------------
"
" Solarized comes with a Toggle Background plugin that by default will map to
" <F5> if that mapping is available. If it is not available you will need to
" either map the function manually or change your current <F5> mapping to
" something else. If you wish to map the function manually, enter the following
" lines in your .vimrc:
"
"     nmap <unique> <F5> <Plug>ToggleBackground
"     imap <unique> <F5> <Plug>ToggleBackground
"     vmap <unique> <F5> <Plug>ToggleBackground
"
" Note that it is important to *not* use the noremap map variants. The plugin
" uses noremap internally. You may run `:help togglebg` for more information.
"
" ---------------------------------------------------------------------
" OPTIONS
" ---------------------------------------------------------------------
"
" Set these in your vimrc file prior to calling the colorscheme.
"
" option name               default     optional
" ------------------------------------------------
" g:solarized_termcolors=   16      |   256
" g:solarized_termtrans =   0       |   1
" g:solarized_degrade   =   0       |   1
" g:solarized_bold      =   1       |   0
" g:solarized_underline =   1       |   0
" g:solarized_italic    =   1       |   0
" g:solarized_contrast  =   "normal"|   "high" or "low"
" g:solarized_visibility=   "normal"|   "high" or "low"
" ------------------------------------------------
"
" OPTION DETAILS
"
" ------------------------------------------------
" g:solarized_termcolors=   256     |   16
" ------------------------------------------------
" The most important option if you are using vim in terminal (non gui) mode!
" This tells Solarized to use the 256 degraded color mode if running in a 256
" color capable terminal.  Otherwise, if set to `16` it will use the terminal
" emulators colorscheme (best option as long as you've set the emulators colors
" to the Solarized palette).
"
" If you are going to use Solarized in Terminal mode (i.e. not in a GUI
" version like gvim or macvim), **please please please** consider setting your
" terminal emulator's colorscheme to used the Solarized palette. I've included
" palettes for some popular terminal emulator as well as Xdefaults in the
" official Solarized download available from:
" http://ethanschoonover.com/solarized . If you use Solarized without these
" colors, Solarized will by default use an approximate set of 256 colors.  It
" isn't bad looking and has been extensively tweaked, but it's still not quite
" the real thing.
"
" ------------------------------------------------
" g:solarized_termtrans =   0       |   1
" ------------------------------------------------
" If you use a terminal emulator with a transparent background and Solarized
" isn't displaying the background color transparently, set this to 1 and
" Solarized will use the default (transparent) background of the terminal
" emulator. *urxvt* required this in my testing; iTerm2 did not.
"
" Note that on Mac OS X Terminal.app, solarized_termtrans is set to 1 by
" default as this is almost always the best option. The only exception to this
" is if the working terminfo file supports 256 colors (xterm-256color).
"
" ------------------------------------------------
" g:solarized_degrade   =   0       |   1
" ------------------------------------------------
" For test purposes only; forces Solarized to use the 256 degraded color mode
" to test the approximate color values for accuracy.
"
" ------------------------------------------------
" g:solarized_bold      =   1       |   0
" ------------------------------------------------
" ------------------------------------------------
" g:solarized_underline =   1       |   0
" ------------------------------------------------
" ------------------------------------------------
" g:solarized_italic    =   1       |   0
" ------------------------------------------------
" If you wish to stop Solarized from displaying bold, underlined or
" italicized typefaces, simply assign a zero value to the appropriate
" variable, for example: `let g:solarized_italic=0`
"
" ------------------------------------------------
" g:solarized_contrast  =   "normal"|   "high" or "low"
" ------------------------------------------------
" Stick with normal! It's been carefully tested. Setting this option to high
" or low does use the same Solarized palette but simply shifts some values up
" or down in order to expand or compress the tonal range displayed.
"
" ------------------------------------------------
" g:solarized_visibility =  "normal"|   "high" or "low"
" ------------------------------------------------
" Special characters such as trailing whitespace, tabs, newlines, when
" displayed using ":set list" can be set to one of three levels depending on
" your needs.
"
" ---------------------------------------------------------------------
" COLOR VALUES
" ---------------------------------------------------------------------
" Download palettes and files from: http://ethanschoonover.com/solarized
"
" L\*a\*b values are canonical (White D65, Reference D50), other values are
" matched in sRGB space.
"
" SOLARIZED HEX     16/8 TERMCOL  XTERM/HEX   L*A*B      sRGB        HSB
" --------- ------- ---- -------  ----------- ---------- ----------- -----------
" base03    #002b36  8/4 brblack  234 #1c1c1c 15 -12 -12   0  43  54 193 100  21
" base02    #073642  0/4 black    235 #262626 20 -12 -12   7  54  66 192  90  26
" base01    #586e75 10/7 brgreen  240 #4e4e4e 45 -07 -07  88 110 117 194  25  46
" base00    #657b83 11/7 bryellow 241 #585858 50 -07 -07 101 123 131 195  23  51
" base0     #839496 12/6 brblue   244 #808080 60 -06 -03 131 148 150 186  13  59
" base1     #93a1a1 14/4 brcyan   245 #8a8a8a 65 -05 -02 147 161 161 180   9  63
" base2     #eee8d5  7/7 white    254 #d7d7af 92 -00  10 238 232 213  44  11  93
" base3     #fdf6e3 15/7 brwhite  230 #ffffd7 97  00  10 253 246 227  44  10  99
" yellow    #b58900  3/3 yellow   136 #af8700 60  10  65 181 137   0  45 100  71
" orange    #cb4b16  9/3 brred    166 #d75f00 50  50  55 203  75  22  18  89  80
" red       #dc322f  1/1 red      160 #d70000 50  65  45 220  50  47   1  79  86
" magenta   #d33682  5/5 magenta  125 #af005f 50  65 -05 211  54 130 331  74  83
" violet    #6c71c4 13/5 brmagenta 61 #5f5faf 50  15 -45 108 113 196 237  45  77
" blue      #268bd2  4/4 blue      33 #0087ff 55 -10 -45  38 139 210 205  82  82
" cyan      #2aa198  6/6 cyan      37 #00afaf 60 -35 -05  42 161 152 175  74  63
" green     #859900  2/2 green     64 #5f8700 60 -20  65 133 153   0  68 100  60
"
" ---------------------------------------------------------------------
" COLORSCHEME HACKING
" ---------------------------------------------------------------------
"
" Useful commands for testing colorschemes:
" :source $VIMRUNTIME/syntax/hitest.vim
" :help highlight-groups
" :help cterm-colors
" :help group-name
"
" Useful links for developing colorschemes:
" http://www.vim.org/scripts/script.php?script_id=2937
" http://vimcasts.org/episodes/creating-colorschemes-for-vim/
" http://www.frexx.de/xterm-256-notes/"
"
"
" }}}
" Default option values"{{{
" ---------------------------------------------------------------------
if !exists("g:solarized_termtrans")
    if ($TERM_PROGRAM ==? "apple_terminal" && &t_Co < 256)
        let g:solarized_termtrans = 1
    else
        let g:solarized_termtrans = 0
    endif
endif
if !exists("g:solarized_degrade")
    let g:solarized_degrade = 0
endif
if !exists("g:solarized_bold")
    let g:solarized_bold = 1
endif
if !exists("g:solarized_underline")
    let g:solarized_underline = 1
endif
if !exists("g:solarized_italic")
    let g:solarized_italic = 1
endif
if !exists("g:solarized_termcolors")
    let g:solarized_termcolors = 16
endif
if !exists("g:solarized_contrast")
    let g:solarized_contrast = "normal"
endif
if !exists("g:solarized_visibility")
    let g:solarized_visibility = "normal"
endif
"}}}
" Colorscheme initialization "{{{
" ---------------------------------------------------------------------
hi clear
if exists("syntax_on")
  syntax reset
endif
let colors_name = "solarized"

"}}}
" GUI & CSApprox hexadecimal palettes"{{{
" ---------------------------------------------------------------------
"
" Set both gui and terminal color values in separate conditional statements
" Due to possibility that CSApprox is running (though I suppose we could just
" leave the hex values out entirely in that case and include only cterm colors)
" We also check to see if user has set solarized (force use of the
" neutral gray monotone palette component)
if (has("gui_running") && g:solarized_degrade == 0)
    let s:vmode       = "gui"
    let s:base03      = "#002b36"
    let s:base02      = "#073642"
    let s:base01      = "#586e75"
    let s:base00      = "#657b83"
    let s:base0       = "#839496"
    let s:base1       = "#93a1a1"
    let s:base2       = "#eee8d5"
    let s:base3       = "#fdf6e3"
    let s:yellow      = "#b58900"
    let s:orange      = "#cb4b16"
    let s:red         = "#dc322f"
    let s:magenta     = "#d33682"
    let s:violet      = "#6c71c4"
    let s:blue        = "#268bd2"
    let s:cyan        = "#2aa198"
    let s:green       = "#859900"
elseif (has("gui_running") && g:solarized_degrade == 1)
    " These colors are identical to the 256 color mode. They may be viewed
    " while in gui mode via "let g:solarized_degrade=1", though this is not
    " recommened and is for testing only.
    let s:vmode       = "gui"
    let s:base03      = "#1c1c1c"
    let s:base02      = "#262626"
    let s:base01      = "#4e4e4e"
    let s:base00      = "#585858"
    let s:base0       = "#808080"
    let s:base1       = "#8a8a8a"
    let s:base2       = "#d7d7af"
    let s:base3       = "#ffffd7"
    let s:yellow      = "#af8700"
    let s:orange      = "#d75f00"
    let s:red         = "#af0000"
    let s:magenta     = "#af005f"
    let s:violet      = "#5f5faf"
    let s:blue        = "#0087ff"
    let s:cyan        = "#00afaf"
    let s:green       = "#5f8700"
elseif g:solarized_termcolors != 256 && &t_Co >= 16
    let s:vmode       = "cterm"
    let s:base03      = "8"
    let s:base02      = "0"
    let s:base01      = "10"
    let s:base00      = "11"
    let s:base0       = "12"
    let s:base1       = "14"
    let s:base2       = "7"
    let s:base3       = "15"
    let s:yellow      = "3"
    let s:orange      = "9"
import os

verbosity = 0
indent_spaces = 4

# we dont want to put color ansi escape sequences
# into redirected stdout (writing to a file, etc)
if os.isatty(1):
    class fgcol:
        BRED = '\033[91m' # bright red
        BYELLOW = '\033[93m' # bright yellow
        BBLUE = '\033[94m' # bright blue
        BMAGENTA = '\033[95m' # bright magenta
        NOCOLOR = '\033[0m'
else:
    class fgcol:
        BRED = '' # bright red
        BYELLOW = '' # bright yellow
        BBLUE = '' # bright blue
        BMAGENTA = '' # bright magenta
        NOCOLOR = ''

def error(msg, indent=0):
    indent_str = " "*indent_spaces*indent
    print(f"[{fgcol.BRED}ERROR{fgcol.NOCOLOR}] {indent_str}{msg}")

def warn(msg, indent=0):
    if verbosity < 1: return
    indent_str = " "*indent_spaces*indent
    print(f"[{fgcol.BYELLOW}WARN{fgcol.NOCOLOR}] {indent_str}{msg}")

def info(msg, indent=0):
    if verbosity < 2: return
    indent_str = " "*indent_spaces*indent
    print(f"[{fgcol.BBLUE}INFO{fgcol.NOCOLOR}] {indent_str}{msg}")

def info2(msg, indent=0):
    if verbosity < 3: return
    indent_str = " "*indent_spaces*indent
    print(f"[{fgcol.BMAGENTA}INFO2{fgcol.NOCOLOR}] {indent_str}{msg}")

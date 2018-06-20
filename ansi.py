END = '\033[0m'
BOLD = '\033[1m'
FAINT = '\033[2m'
ITALIC = '\033[3m'
UNDERLINE = '\033[4m'
SLOWBLINK = '\033[5m'
RAPIDBLINK = '\033[6m'
CROSSEDOUT = '\033[9m'
DEFAULT = '\033[10m'
FONTONE = '\033[11m'
FONTTWO = '\033[12m'
FONTTHREE = '\033[13m'
FONTFOUR = '\033[14m'
FONTFIVE = '\033[15m'
FONTSIX = '\033[16m'
FONTSEVEN = '\033[17m'
FONTEIGHT = '\033[18m'
FONTNINE = '\033[19m'
BLACK = '\033[30m'
DARKRED = '\033[31m'
DARKGREEN = '\033[32m'
DARKYELLOW = '\033[33m'
DARKBLUE = '\033[34m'
DARKMAGENTA = '\033[35m'
DARKCYAN = '\033[36m'
LIGHTGRAY = '\033[37m'
DARKGRAY = '\033[90m'
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'


def regular(string=None):
    if string is None:
        return END
    elif string:
        return END + string
    else:
        raise TypeError


def bold(string=None):
    if string is None:
        return BOLD
    elif string:
        return BOLD + string
    else:
        raise TypeError


def faint(string=None):
    if string is None:
        return FAINT
    elif string:
        return FAINT + string
    else:
        raise TypeError


def italicize(string=None):
    if string is None:
        return ITALIC
    elif string:
        return ITALIC + string
    else:
        raise TypeError


def underline(string=None):
    if string is None:
        return UNDERLINE
    elif string:
        return UNDERLINE + string
    else:
        raise TypeError


def slow_blink(string=None):
    if string is None:
        return SLOWBLINK
    elif string:
        return SLOWBLINK + string
    else:
        raise TypeError


def rapid_blink(string=None):
    if string is None:
        return RAPIDBLINK
    elif string:
        return RAPIDBLINK + string
    else:
        raise TypeError


def cross_out(string=None):
    if string is None:
        return CROSSEDOUT
    elif string:
        return CROSSEDOUT + string
    else:
        raise TypeError


def default_font(string=None):
    if string is None:
        return DEFAULT
    elif string:
        return DEFAULT + string
    else:
        raise TypeError


def font_one(string=None):
    if string is None:
        return FONTONE
    elif string:
        return FONTONE + string
    else:
        raise TypeError


def font_two(string=None):
    if string is None:
        return FONTTWO
    elif string:
        return FONTTWO + string
    else:
        raise TypeError


def font_three(string=None):
    if string is None:
        return FONTTHREE
    elif string:
        return FONTTHREE + string
    else:
        raise TypeError


def font_four(string=None):
    if string is None:
        return FONTFOUR
    elif string:
        return FONTFOUR + string
    else:
        raise TypeError


def font_five(string=None):
    if string is None:
        return FONTFIVE
    elif string:
        return FONTFIVE + string
    else:
        raise TypeError


def font_six(string=None):
    if string is None:
        return FONTSIX
    elif string:
        return FONTSIX + string
    else:
        raise TypeError


def font_seven(string=None):
    if string is None:
        return FONTSEVEN
    elif string:
        return FONTSEVEN + string
    else:
        raise TypeError


def font_eight(string=None):
    if string is None:
        return FONTEIGHT
    elif string:
        return FONTEIGHT + string
    else:
        raise TypeError


def font_nine(string=None):
    if string is None:
        return FONTNINE
    elif string:
        return FONTNINE + string
    else:
        raise TypeError


def black(string=None):
    if string is None:
        return BLACK
    elif string:
        return BLACK + string
    else:
        raise TypeError


def dark_red(string=None):
    if string is None:
        return DARKRED
    elif string:
        return DARKRED + string
    else:
        raise TypeError


def dark_green(string=None):
    if string is None:
        return DARKGREEN
    elif string:
        return DARKGREEN + string
    else:
        raise TypeError


def dark_yellow(string=None):
    if string is None:
        return DARKYELLOW
    elif string:
        return DARKYELLOW + string
    else:
        raise TypeError


def dark_blue(string=None):
    if string is None:
        return DARKBLUE
    elif string:
        return DARKBLUE + string
    else:
        raise TypeError


def dark_magenta(string=None):
    if string is None:
        return DARKMAGENTA
    elif string:
        return DARKMAGENTA + string
    else:
        raise TypeError


def dark_cyan(string=None):
    if string is None:
        return DARKCYAN
    elif string:
        return DARKCYAN + string
    else:
        raise TypeError


def light_gray(string=None):
    if string is None:
        return LIGHTGRAY
    elif string:
        return LIGHTGRAY + string
    else:
        raise TypeError


def dark_gray(string=None):
    if string is None:
        return DARKGRAY
    elif string:
        return DARKGRAY + string
    else:
        raise TypeError


def red(string=None):
    if string is None:
        return RED
    elif string:
        return RED + string
    else:
        raise TypeError


def green(string=None):
    if string is None:
        return GREEN
    elif string:
        return GREEN + string
    else:
        raise TypeError


def yellow(string=None):
    if string is None:
        return YELLOW
    elif string:
        return YELLOW + string
    else:
        raise TypeError


def blue(string=None):
    if string is None:
        return BLUE
    elif string:
        return BLUE + string
    else:
        raise TypeError


def magenta(string=None):
    if string is None:
        return MAGENTA
    elif string:
        return MAGENTA + string
    else:
        raise TypeError


def cyan(string=None):
    if string is None:
        return CYAN
    elif string:
        return CYAN + string
    else:
        raise TypeError


def white(string=None):
    if string is None:
        return WHITE
    elif string:
        return WHITE + string
    else:
        raise TypeError

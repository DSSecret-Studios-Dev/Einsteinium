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
    """
    Changes Text in Terminal to Default

    :param string: Inputted String
    :type string: str
    :return: ANSI Escape Code for END
    :rtype: str
    :raises TypeError: Incorrect Parameter Type Inputted
    """

    if not string:
        return END
    elif isinstance(string, str):
        return END + string
    else:
        raise TypeError


def bold(string=None):
    """
    Bolds Text in Terminal

    :param string: Inputted String
    :type string: str
    :return: ANSI Escape Code for BOLD
    :rtype: str
    :raises TypeError: Incorrect Parameter Type Inputted
    """

    if not string:
        return BOLD
    elif isinstance(string, str):
        return BOLD + string
    else:
        raise TypeError


def faint(string=None):
    """
    Lightens Text in Terminal

    :param string: Inputted String
    :type string: str
    :return: ANSI Escape Code for FAINT
    :rtype: str
    :raises TypeError: Incorrect Parameter Type Inputted
    """

    if not string:
        return FAINT
    elif isinstance(string, str):
        return FAINT + string
    else:
        raise TypeError


def italicize(string=None):
    """
    Italicizes Text in Terminal

    :param string: Inputted String
    :type string: str
    :return: ANSI Escape Code for Italics
    :rtype: str
    :raises TypeError: Incorrect Parameter Type Inputted
    """

    if not string:
        return ITALIC
    elif isinstance(string, str):
        return ITALIC + string
    else:
        raise TypeError


def underline(string=None):
    """
    Underlines Text in Terminal

    :param string: Inputted String
    :type string: str
    :return: ANSI Escape Code for Underline
    :rtype: str
    :raises TypeError: Incorrect Parameter Type Inputted"""

    if not string:
        return UNDERLINE
    elif isinstance(string, str):
        return UNDERLINE + string
    else:
        raise TypeError


def slow_blink(string=None):
    """
    Slowly Blinks Text in Terminal

    :param string: Inputted String
    :type string: str
    :return: ANSI Escape Code for Slow Blink
    :rtype: str
    :raises TypeError: Incorrect Parameter Type Inputted"""
    if not string:
        return SLOWBLINK
    elif isinstance(string, str):
        return SLOWBLINK + string
    else:
        raise TypeError


def rapid_blink(string=None):
    """
    Rapidly Blinks Text in Terminal

    :param string: Inputted String
    :type string: str
    :return: ANSI Escape Code for Rapid Blink
    :rtype: str
    :raises TypeError: Incorrect Parameter Type Inputted"""

    if not string:
        return RAPIDBLINK
    elif isinstance(string, str):
        return RAPIDBLINK + string
    else:
        raise TypeError


def cross_out(string=None):
    """
    Crosses Out Text in Terminal

    :param string: Inputted String
    :type string: str
    :return: ANSI Escape Code for Crossed-out
    :rtype: str
    :raises TypeError: Incorrect Parameter Type Inputted"""

    if not string:
        return CROSSEDOUT
    elif isinstance(string, str):
        return CROSSEDOUT + string
    else:
        raise TypeError


def default_font(string=None):
    """
    Changes Text's Font to Default

    :param string: Inputted String
    :type string: str
    :return: ANSI Escape Code for Default Font
    :rtype: str
    :raises TypeError: Incorrect Parameter Type Inputted"""

    if not string:
        return DEFAULT
    elif isinstance(string, str):
        return DEFAULT + string
    else:
        raise TypeError


def font_one(string=None):
    """
    Change Text's Font to Font One

    :param string: Inputted String
    :type string: str
    :return: ANSI Escape Code for Font One
    :rtype: str
    :raises TypeError: Incorrect Parameter Type Inputted"""

    if not string:
        return FONTONE
    elif isinstance(string, str):
        return FONTONE + string
    else:
        raise TypeError


def font_two(string=None):
    """
    Changes Text's Font to Font Two

    :param string: Inputted String
    :type string: str
    :return: ANSI Escape Code for Font Two
    :rtype: str
    :raises TypeError: Incorrect Parameter Type Inputted"""

    if not string:
        return FONTTWO
    elif isinstance(string, str):
        return FONTTWO + string
    else:
        raise TypeError


def font_three(string=None):
    """
    Changes Text's Font to Font Three

    :param string: Inputted String
    :type string: str
    :return: ANSI Escape Code for Font Three
    :rtype: str
    :raises TypeError: Incorrect Parameter Type Inputted"""

    if not string:
        return FONTTHREE
    elif isinstance(string, str):
        return FONTTHREE + string
    else:
        raise TypeError


def font_four(string=None):
    """
    Changes Text's Font to Font Four

    :param string: Inputted String
    :type string: str
    :return: ANSI Escape Code for Font Four
    :rtype: str
    :raises TypeError: Incorrect Parameter Type Inputted"""

    if not string:
        return FONTFOUR
    elif isinstance(string, str):
        return FONTFOUR + string
    else:
        raise TypeError


def font_five(string=None):
    """
    Changes Text's Font to Font Five

    :param string: Inputted String
    :type string: str
    :return: ANSI Escape Code for Font Five
    :rtype: str
    :raises TypeError: Incorrect Parameter Type Inputted"""

    if not string:
        return FONTFIVE
    elif isinstance(string, str):
        return FONTFIVE + string
    else:
        raise TypeError


def font_six(string=None):
    """
    Changes Text's Font to Font Six

    :param string: Inputted String
    :type string: str
    :return: ANSI Escape Code for Font Six
    :rtype: str
    :raises TypeError: Incorrect Parameter Type Inputted"""

    if not string:
        return FONTSIX
    elif isinstance(string, str):
        return FONTSIX + string
    else:
        raise TypeError


def font_seven(string=None):
    """
    Changes Text's Font to Font Seven

    :param string: Inputted String
    :type string: str
    :return: ANSI Escape Code for Font Seven
    :rtype: str
    :raises TypeError: Incorrect Parameter Type Inputted"""

    if not string:
        return FONTSEVEN
    elif isinstance(string, str):
        return FONTSEVEN + string
    else:
        raise TypeError


def font_eight(string=None):
    """
    Changes Text's Font to Font Eight

    :param string: Inputted String
    :type string: str
    :return: ANSI Escape Code for Font Eight
    :rtype: str
    :raises TypeError: Incorrect Parameter Type Inputted"""

    if not string:
        return FONTEIGHT
    elif isinstance(string, str):
        return FONTEIGHT + string
    else:
        raise TypeError


def font_nine(string=None):
    """
    Changes Text's Font to Font Nine

    :param string: Inputted String
    :type string: str
    :return: ANSI Escape Code for Font Nine
    :rtype: str
    :raises TypeError: Incorrect Parameter Type Inputted"""

    if not string:
        return FONTNINE
    elif isinstance(string, str):
        return FONTNINE + string
    else:
        raise TypeError


def black(string=None):
    """
    Changes Text's Color to Black

    :param string: Inputted String
    :type string: str
    :return: ANSI Escape Code for Black
    :rtype: str
    :raises TypeError: Incorrect Parameter Type Inputted"""

    if not string:
        return BLACK
    elif isinstance(string, str):
        return BLACK + string
    else:
        raise TypeError


def dark_red(string=None):
    """
    Changes Text's Color to Dark Red

    :param string: Inputted String
    :type string: str
    :return: ANSI Escape Code for Dark Red
    :rtype: str
    :raises TypeError: Incorrect Parameter Type Inputted"""

    if not string:
        return DARKRED
    elif isinstance(string, str):
        return DARKRED + string
    else:
        raise TypeError


def dark_green(string=None):
    """
    Changes Text's Color to Dark Green

    :param string: Inputted String
    :type string: str
    :return: ANSI Escape Code for Dark Green
    :rtype: str
    :raises TypeError: Incorrect Parameter Type Inputted"""

    if not string:
        return DARKGREEN
    elif isinstance(string, str):
        return DARKGREEN + string
    else:
        raise TypeError


def dark_yellow(string=None):
    """
    Changes Text's Color to Dark Yellow

    :param string: Inputted String
    :type string: str
    :return: ANSI Escape Code for Dark Yellow
    :rtype: str
    :raises TypeError: Incorrect Parameter Type Inputted"""

    if not string:
        return DARKYELLOW
    elif isinstance(string, str):
        return DARKYELLOW + string
    else:
        raise TypeError


def dark_blue(string=None):
    """
    Changes Text's Color to Dark Blue

    :param string: Inputted String
    :type string: str
    :return: ANSI Escape Code for Dark Blue
    :rtype: str
    :raises TypeError: Incorrect Parameter Type Inputted"""

    if not string:
        return DARKBLUE
    elif isinstance(string, str):
        return DARKBLUE + string
    else:
        raise TypeError


def dark_magenta(string=None):
    """
    Changes Text's Color to Dark Magenta

    :param string: Inputted String
    :type string: str
    :return: ANSI Escape Code for Dark Magenta
    :rtype: str
    :raises TypeError: Incorrect Parameter Type Inputted"""

    if not string:
        return DARKMAGENTA
    elif isinstance(string, str):
        return DARKMAGENTA + string
    else:
        raise TypeError


def dark_cyan(string=None):
    """
    Changes Text's Color to Dark Cyan

    :param string: Inputted String
    :type string: str
    :return: ANSI Escape Code for Dark Cyan
    :rtype: str
    :raises TypeError: Incorrect Parameter Type Inputted"""

    if not string:
        return DARKCYAN
    elif isinstance(string, str):
        return DARKCYAN + string
    else:
        raise TypeError


def light_gray(string=None):
    """
    Changes Text's Color to Light Gray

    :param string: Inputted String
    :type string: str
    :return: ANSI Escape Code for Light Gray
    :rtype: str
    :raises TypeError: Incorrect Parameter Type Inputted"""

    if not string:
        return LIGHTGRAY
    elif isinstance(string, str):
        return LIGHTGRAY + string
    else:
        raise TypeError


def dark_gray(string=None):
    """
    Changes Text's Color to Dark Gray

    :param string: Inputted String
    :type string: str
    :return: ANSI Escape Code for Dark Gray
    :rtype: str
    :raises TypeError: Incorrect Parameter Type Inputted"""

    if not string:
        return DARKGRAY
    elif isinstance(string, str):
        return DARKGRAY + string
    else:
        raise TypeError


def red(string=None):
    """
    Changes Text's Color to Red

    :param string: Inputted String
    :type string: str
    :return: ANSI Escape Code for Red
    :rtype: str
    :raises TypeError: Incorrect Parameter Type Inputted"""

    if not string:
        return RED
    elif isinstance(string, str):
        return RED + string
    else:
        raise TypeError


def green(string=None):
    """
    Changes Text's Color to Green

    :param string: Inputted String
    :type string: str
    :return: ANSI Escape Code for Green
    :rtype: str
    :raises TypeError: Incorrect Parameter Type Inputted"""

    if not string:
        return GREEN
    elif isinstance(string, str):
        return GREEN + string
    else:
        raise TypeError


def yellow(string=None):
    """
    Changes Text's Color to Yellow

    :param string: Inputted String
    :type string: str
    :return: ANSI Escape Code for Yellow
    :rtype: str
    :raises TypeError: Incorrect Parameter Type Inputted"""

    if not string:
        return YELLOW
    elif isinstance(string, str):
        return YELLOW + string
    else:
        raise TypeError


def blue(string=None):
    """
    Changes Text's Color to Blue

    :param string: Inputted String
    :type string: str
    :return: ANSI Escape Code for Blue
    :rtype: str
    :raises TypeError: Incorrect Parameter Type Inputted"""

    if not string:
        return BLUE
    elif isinstance(string, str):
        return BLUE + string
    else:
        raise TypeError


def magenta(string=None):
    """
    Changes Text's Color to Magenta

    :param string: Inputted String
    :type string: str
    :return: ANSI Escape Code for Magenta
    :rtype: str
    :raises TypeError: Incorrect Parameter Type Inputted"""

    if not string:
        return MAGENTA
    elif isinstance(string, str):
        return MAGENTA + string
    else:
        raise TypeError


def cyan(string=None):
    """
    Changes Text's Color to Cyan

    :param string: Inputted String
    :type string: str
    :return: ANSI Escape Code for Cyan
    :rtype: str
    :raises TypeError: Incorrect Parameter Type Inputted"""

    if not string:
        return CYAN
    elif isinstance(string, str):
        return CYAN + string
    else:
        raise TypeError


def white(string=None):
    """
    Changes Text's Color to White

    :param string: Inputted String
    :type string: str
    :return: ANSI Escape Code for White
    :rtype: str
    :raises TypeError: Incorrect Parameter Type Inputted"""

    if not string:
        return WHITE
    elif isinstance(string, str):
        return WHITE + string
    else:
        raise TypeError

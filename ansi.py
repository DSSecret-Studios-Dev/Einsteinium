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


def regular(string=None, end=True):
    """
    Changes Text in Terminal to Default

    :param string: Inputted String
    :param end: Adds the ANSI Escape Code for END to Make Text After It Normal
    :type string: str
    :type end: bool
    :return: ANSI Escape Code for END
    :rtype: str
    :raises TypeError: Incorrect Parameter Type Inputted
    """

    if not string:
        return END
    elif isinstance(string, str):
        if end:
            return END + string + END
        elif not end:
            return END + string
        else:
            raise TypeError
    else:
        raise TypeError


def bold(string=None, end=True):
    """
    Bolds Text in Terminal

    :param string: Inputted String
    :param end: Adds the ANSI Escape Code for END to Make Text After It Normal
    :type string: str
    :type end: bool
    :return: ANSI Escape Code for BOLD
    :rtype: str
    :raises TypeError: Incorrect Parameter Type Inputted
    """

    if not string:
        return BOLD
    elif isinstance(string, str):
        if end:
            return BOLD + string + END
        elif not end:
            return BOLD + string
        else:
            raise TypeError
    else:
        raise TypeError


def faint(string=None, end=True):
    """
    Lightens Text in Terminal

    :param string: Inputted String
    :param end: Adds the ANSI Escape Code for END to Make Text After It Normal
    :type string: str
    :type end: bool
    :return: ANSI Escape Code for FAINT
    :rtype: str
    :raises TypeError: Incorrect Parameter Type Inputted
    """

    if not string:
        return FAINT
    elif isinstance(string, str):
        if end:
            return FAINT + string + END
        elif not end:
            return FAINT + string
        else:
            raise TypeError
    else:
        raise TypeError


def italicize(string=None, end=True):
    """
    Italicizes Text in Terminal

    :param string: Inputted String
    :param end: Adds the ANSI Escape Code for END to Make Text After It Normal
    :type string: str
    :type end: bool
    :return: ANSI Escape Code for Italics
    :rtype: str
    :raises TypeError: Incorrect Parameter Type Inputted
    """

    if not string:
        return ITALIC
    elif isinstance(string, str):
        if end:
            return ITALIC + string + END
        elif not end:
            return ITALIC + string
        else:
            raise TypeError
    else:
        raise TypeError


def underline(string=None, end=True):
    """
    Underlines Text in Terminal

    :param string: Inputted String
    :param end: Adds the ANSI Escape Code for END to Make Text After It Normal
    :type string: str
    :type end: bool
    :return: ANSI Escape Code for Underline
    :rtype: str
    :raises TypeError: Incorrect Parameter Type Inputted"""

    if not string:
        return UNDERLINE
    elif isinstance(string, str):
        if end:
            return UNDERLINE + string + END
        elif not end:
            return UNDERLINE + string
        else:
            raise TypeError
    else:
        raise TypeError


def slow_blink(string=None, end=True):
    """
    Slowly Blinks Text in Terminal

    :param string: Inputted String
    :param end: Adds the ANSI Escape Code for END to Make Text After It Normal
    :type string: str
    :type end: bool
    :return: ANSI Escape Code for Slow Blink
    :rtype: str
    :raises TypeError: Incorrect Parameter Type Inputted"""
    if not string:
        return SLOWBLINK
    elif isinstance(string, str):
        if end:
            return SLOWBLINK + string + END
        elif not end:
            return SLOWBLINK + string
        else:
            raise TypeError
    else:
        raise TypeError


def rapid_blink(string=None, end=True):
    """
    Rapidly Blinks Text in Terminal

    :param string: Inputted String
    :param end: Adds the ANSI Escape Code for END to Make Text After It Normal
    :type string: str
    :type end: bool
    :return: ANSI Escape Code for Rapid Blink
    :rtype: str
    :raises TypeError: Incorrect Parameter Type Inputted"""

    if not string:
        return RAPIDBLINK
    elif isinstance(string, str):
        if end:
            return RAPIDBLINK + string + END
        elif not end:
            return RAPIDBLINK + string
        else:
            raise TypeError
    else:
        raise TypeError


def cross_out(string=None, end=True):
    """
    Crosses Out Text in Terminal

    :param string: Inputted String
    :param end: Adds the ANSI Escape Code for END to Make Text After It Normal
    :type string: str
    :type end: bool
    :return: ANSI Escape Code for Crossed-out
    :rtype: str
    :raises TypeError: Incorrect Parameter Type Inputted"""

    if not string:
        return CROSSEDOUT
    elif isinstance(string, str):
        if end:
            return CROSSEDOUT + string + END
        elif not end:
            return CROSSEDOUT + string
        else:
            raise TypeError
    else:
        raise TypeError


def default_font(string=None, end=True):
    """
    Changes Text's Font to Default

    :param string: Inputted String
    :param end: Adds the ANSI Escape Code for END to Make Text After It Normal
    :type string: str
    :type end: bool
    :return: ANSI Escape Code for Default Font
    :rtype: str
    :raises TypeError: Incorrect Parameter Type Inputted"""

    if not string:
        return DEFAULT
    elif isinstance(string, str):
        if end:
            return DEFAULT + string + END
        elif not end:
            return DEFAULT + string
        else:
            raise TypeError
    else:
        raise TypeError


def font_one(string=None, end=True):
    """
    Change Text's Font to Font One

    :param string: Inputted String
    :param end: Adds the ANSI Escape Code for END to Make Text After It Normal
    :type string: str
    :type end: bool
    :return: ANSI Escape Code for Font One
    :rtype: str
    :raises TypeError: Incorrect Parameter Type Inputted"""

    if not string:
        return FONTONE
    elif isinstance(string, str):
        if end:
            return FONTONE + string + END
        elif not end:
            return FONTONE + string
        else:
            raise TypeError
    else:
        raise TypeError


def font_two(string=None, end=True):
    """
    Changes Text's Font to Font Two

    :param string: Inputted String
    :param end: Adds the ANSI Escape Code for END to Make Text After It Normal
    :type string: str
    :type end: bool
    :return: ANSI Escape Code for Font Two
    :rtype: str
    :raises TypeError: Incorrect Parameter Type Inputted"""

    if not string:
        return FONTTWO
    elif isinstance(string, str):
        if end:
            return FONTTWO + string + END
        elif not end:
            return FONTTWO + string
        else:
            raise TypeError
    else:
        raise TypeError


def font_three(string=None, end=True):
    """
    Changes Text's Font to Font Three

    :param string: Inputted String
    :param end: Adds the ANSI Escape Code for END to Make Text After It Normal
    :type string: str
    :type end: bool
    :return: ANSI Escape Code for Font Three
    :rtype: str
    :raises TypeError: Incorrect Parameter Type Inputted"""

    if not string:
        return FONTTHREE
    elif isinstance(string, str):
        if end:
            return FONTTHREE + string + END
        elif not end:
            return FONTTHREE + string
        else:
            raise TypeError
    else:
        raise TypeError


def font_four(string=None, end=True):
    """
    Changes Text's Font to Font Four

    :param string: Inputted String
    :param end: Adds the ANSI Escape Code for END to Make Text After It Normal
    :type string: str
    :type end: bool
    :return: ANSI Escape Code for Font Four
    :rtype: str
    :raises TypeError: Incorrect Parameter Type Inputted"""

    if not string:
        return FONTFOUR
    elif isinstance(string, str):
        if end:
            return FONTFIVE + string + END
        elif not end:
            return FONTFOUR + string
        else:
            raise TypeError
    else:
        raise TypeError


def font_five(string=None, end=True):
    """
    Changes Text's Font to Font Five

    :param string: Inputted String
    :param end: Adds the ANSI Escape Code for END to Make Text After It Normal
    :type string: str
    :type end: bool
    :return: ANSI Escape Code for Font Five
    :rtype: str
    :raises TypeError: Incorrect Parameter Type Inputted"""

    if not string:
        return FONTFIVE
    elif isinstance(string, str):
        if end:
            return FONTFIVE + string + END
        elif not end:
            return FONTFIVE + string
        else:
            raise TypeError
    else:
        raise TypeError


def font_six(string=None, end=True):
    """
    Changes Text's Font to Font Six

    :param string: Inputted String
    :param end: Adds the ANSI Escape Code for END to Make Text After It Normal
    :type string: str
    :type end: bool
    :return: ANSI Escape Code for Font Six
    :rtype: str
    :raises TypeError: Incorrect Parameter Type Inputted"""

    if not string:
        return FONTSIX
    elif isinstance(string, str):
        if end:
            return FONTSIX + string + END
        elif not end:
            return FONTSIX + string
        else:
            raise TypeError
    else:
        raise TypeError


def font_seven(string=None, end=True):
    """
    Changes Text's Font to Font Seven

    :param string: Inputted String
    :param end: Adds the ANSI Escape Code for END to Make Text After It Normal
    :type string: str
    :type end: bool
    :return: ANSI Escape Code for Font Seven
    :rtype: str
    :raises TypeError: Incorrect Parameter Type Inputted"""

    if not string:
        return FONTSEVEN
    elif isinstance(string, str):
        if end:
            return FONTSEVEN + string + END
        elif not end:
            return FONTSEVEN + string
        else:
            raise TypeError
    else:
        raise TypeError


def font_eight(string=None, end=True):
    """
    Changes Text's Font to Font Eight

    :param string: Inputted String
    :param end: Adds the ANSI Escape Code for END to Make Text After It Normal
    :type string: str
    :type end: bool
    :return: ANSI Escape Code for Font Eight
    :rtype: str
    :raises TypeError: Incorrect Parameter Type Inputted"""

    if not string:
        return FONTEIGHT
    elif isinstance(string, str):
        if end:
            return FONTEIGHT + string + END
        elif not end:
            return FONTEIGHT + string
        else:
            raise TypeError
    else:
        raise TypeError


def font_nine(string=None, end=True):
    """
    Changes Text's Font to Font Nine

    :param string: Inputted String
    :param end: Adds the ANSI Escape Code for END to Make Text After It Normal
    :type string: str
    :type end: bool
    :return: ANSI Escape Code for Font Nine
    :rtype: str
    :raises TypeError: Incorrect Parameter Type Inputted"""

    if not string:
        return FONTNINE
    elif isinstance(string, str):
        if end:
            return FONTNINE + string + END
        elif not end:
            return FONTNINE + string
        else:
            raise TypeError
    else:
        raise TypeError


def black(string=None, end=True):
    """
    Changes Text's Color to Black

    :param string: Inputted String
    :param end: Adds the ANSI Escape Code for END to Make Text After It Normal
    :type string: str
    :type end: bool
    :return: ANSI Escape Code for Black
    :rtype: str
    :raises TypeError: Incorrect Parameter Type Inputted"""

    if not string:
        return BLACK
    elif isinstance(string, str):
        if end:
            return BLACK + string + END
        elif not end:
            return BLACK + string
        else:
            raise TypeError
    else:
        raise TypeError


def dark_red(string=None, end=True):
    """
    Changes Text's Color to Dark Red

    :param string: Inputted String
    :param end: Adds the ANSI Escape Code for END to Make Text After It Normal
    :type string: str
    :type end: bool
    :return: ANSI Escape Code for Dark Red
    :rtype: str
    :raises TypeError: Incorrect Parameter Type Inputted"""

    if not string:
        return DARKRED
    elif isinstance(string, str):
        if end:
            return DARKRED + string + END
        elif not end:
            return DARKRED + string
        else:
            raise TypeError
    else:
        raise TypeError


def dark_green(string=None, end=True):
    """
    Changes Text's Color to Dark Green

    :param string: Inputted String
    :param end: Adds the ANSI Escape Code for END to Make Text After It Normal
    :type string: str
    :type end: bool
    :return: ANSI Escape Code for Dark Green
    :rtype: str
    :raises TypeError: Incorrect Parameter Type Inputted"""

    if not string:
        return DARKGREEN
    elif isinstance(string, str):
        if end:
            return DARKGREEN + string + END
        elif not end:
            return DARKGREEN + string
        else:
            raise TypeError
    else:
        raise TypeError


def dark_yellow(string=None, end=True):
    """
    Changes Text's Color to Dark Yellow

    :param string: Inputted String
    :param end: Adds the ANSI Escape Code for END to Make Text After It Normal
    :type string: str
    :type end: bool
    :return: ANSI Escape Code for Dark Yellow
    :rtype: str
    :raises TypeError: Incorrect Parameter Type Inputted"""

    if not string:
        return DARKYELLOW
    elif isinstance(string, str):
        if end:
            return DARKYELLOW + string + END
        elif not end:
            return DARKYELLOW + string
        else:
            raise TypeError
    else:
        raise TypeError


def dark_blue(string=None, end=True):
    """
    Changes Text's Color to Dark Blue

    :param string: Inputted String
    :param end: Adds the ANSI Escape Code for END to Make Text After It Normal
    :type string: str
    :type end: bool
    :return: ANSI Escape Code for Dark Blue
    :rtype: str
    :raises TypeError: Incorrect Parameter Type Inputted"""

    if not string:
        return DARKBLUE
    elif isinstance(string, str):
        if end:
            return DARKBLUE + string + END
        elif not end:
            return DARKBLUE + string
        else:
            raise TypeError
    else:
        raise TypeError


def dark_magenta(string=None, end=True):
    """
    Changes Text's Color to Dark Magenta

    :param string: Inputted String
    :param end: Adds the ANSI Escape Code for END to Make Text After It Normal
    :type string: str
    :type end: bool
    :return: ANSI Escape Code for Dark Magenta
    :rtype: str
    :raises TypeError: Incorrect Parameter Type Inputted"""

    if not string:
        return DARKMAGENTA
    elif isinstance(string, str):
        if end:
            return DARKMAGENTA + string + END
        elif not end:
            return DARKMAGENTA + string
        else:
            raise TypeError
    else:
        raise TypeError


def dark_cyan(string=None, end=True):
    """
    Changes Text's Color to Dark Cyan

    :param string: Inputted String
    :param end: Adds the ANSI Escape Code for END to Make Text After It Normal
    :type string: str
    :type end: bool
    :return: ANSI Escape Code for Dark Cyan
    :rtype: str
    :raises TypeError: Incorrect Parameter Type Inputted"""

    if not string:
        return DARKCYAN
    elif isinstance(string, str):
        if end:
            return DARKCYAN + string + END
        elif not end:
            return DARKCYAN + string
        else:
            raise TypeError
    else:
        raise TypeError


def light_gray(string=None, end=True):
    """
    Changes Text's Color to Light Gray

    :param string: Inputted String
    :param end: Adds the ANSI Escape Code for END to Make Text After It Normal
    :type string: str
    :type end: bool
    :return: ANSI Escape Code for Light Gray
    :rtype: str
    :raises TypeError: Incorrect Parameter Type Inputted"""

    if not string:
        return LIGHTGRAY
    elif isinstance(string, str):
        if end:
            return LIGHTGRAY + string + END
        elif not end:
            return LIGHTGRAY + string
        else:
            raise TypeError
    else:
        raise TypeError


def dark_gray(string=None, end=True):
    """
    Changes Text's Color to Dark Gray

    :param string: Inputted String
    :param end: Adds the ANSI Escape Code for END to Make Text After It Normal
    :type string: str
    :type end: bool
    :return: ANSI Escape Code for Dark Gray
    :rtype: str
    :raises TypeError: Incorrect Parameter Type Inputted"""

    if not string:
        return DARKGRAY
    elif isinstance(string, str):
        if end:
            return DARKGRAY + string + END
        elif not end:
            return DARKGRAY + string
        else:
            raise TypeError
    else:
        raise TypeError


def red(string=None, end=True):
    """
    Changes Text's Color to Red

    :param string: Inputted String
    :param end: Adds the ANSI Escape Code for END to Make Text After It Normal
    :type string: str
    :type end: bool
    :return: ANSI Escape Code for Red
    :rtype: str
    :raises TypeError: Incorrect Parameter Type Inputted"""

    if not string:
        return RED
    elif isinstance(string, str):
        if end:
            return RED + string + END
        elif not end:
            return RED + string
        else:
            raise TypeError
    else:
        raise TypeError


def green(string=None, end=True):
    """
    Changes Text's Color to Green

    :param string: Inputted String
    :param end: Adds the ANSI Escape Code for END to Make Text After It Normal
    :type string: str
    :type end: bool
    :return: ANSI Escape Code for Green
    :rtype: str
    :raises TypeError: Incorrect Parameter Type Inputted"""

    if not string:
        return GREEN
    elif isinstance(string, str):
        if end:
            return GREEN + string + END
        elif not end:
            return GREEN + string
        else:
            raise TypeError
    else:
        raise TypeError


def yellow(string=None, end=True):
    """
    Changes Text's Color to Yellow

    :param string: Inputted String
    :param end: Adds the ANSI Escape Code for END to Make Text After It Normal
    :type string: str
    :type end: bool
    :return: ANSI Escape Code for Yellow
    :rtype: str
    :raises TypeError: Incorrect Parameter Type Inputted"""

    if not string:
        return YELLOW
    elif isinstance(string, str):
        if end:
            return YELLOW + string + END
        elif not end:
            return YELLOW + string
        else:
            raise TypeError
    else:
        raise TypeError


def blue(string=None, end=True):
    """
    Changes Text's Color to Blue

    :param string: Inputted String
    :param end: Adds the ANSI Escape Code for END to Make Text After It Normal
    :type string: str
    :type end: bool
    :return: ANSI Escape Code for Blue
    :rtype: str
    :raises TypeError: Incorrect Parameter Type Inputted"""

    if not string:
        return BLUE
    elif isinstance(string, str):
        if end:
            return BLUE + string + END
        elif not end:
            return BLUE + string
        else:
            raise TypeError
    else:
        raise TypeError


def magenta(string=None, end=True):
    """
    Changes Text's Color to Magenta

    :param string: Inputted String
    :param end: Adds the ANSI Escape Code for END to Make Text After It Normal
    :type string: str
    :type end: bool
    :return: ANSI Escape Code for Magenta
    :rtype: str
    :raises TypeError: Incorrect Parameter Type Inputted"""

    if not string:
        return MAGENTA
    elif isinstance(string, str):
        if end:
            return MAGENTA + string + END
        elif not end:
            return MAGENTA + string
        else:
            raise TypeError
    else:
        raise TypeError


def cyan(string=None, end=True):
    """
    Changes Text's Color to Cyan

    :param string: Inputted String
    :param end: Adds the ANSI Escape Code for END to Make Text After It Normal
    :type string: str
    :type end: bool
    :return: ANSI Escape Code for Cyan
    :rtype: str
    :raises TypeError: Incorrect Parameter Type Inputted"""

    if not string:
        return CYAN
    elif isinstance(string, str):
        if end:
            return CYAN + string + END
        elif not end:
            return CYAN + string
        else:
            raise TypeError
    else:
        raise TypeError


def white(string=None, end=True):
    """
    Changes Text's Color to White

    :param string: Inputted String
    :param end: Adds the ANSI Escape Code for END to Make Text After It Normal
    :type string: str
    :type end: bool
    :return: ANSI Escape Code for White
    :rtype: str
    :raises TypeError: Incorrect Parameter Type Inputted"""

    if not string:
        return WHITE
    elif isinstance(string, str):
        if end:
            return WHITE + string + END
        elif not end:
            return WHITE + string
        else:
            raise TypeError
    else:
        raise TypeError


def dark_rainbow(string="Hello, World!", end=True):
    """
    Creates a Rainbow of the Text in the String in the Dark Colors

    :param string: Inputted String
    :param end: Adds the ANSI Escape Code for END to Make Text After It Normal
    :type string: str
    :type end: bool
    :return: Eight Strings of Eight Colors
    :rtype: str
    :raises TypeError: Incorrect Parameter Type Inputted"""

    if isinstance(string, str):
        if isinstance(end, bool):
            return black(string, end) + dark_red(string, end) + dark_green(string, end) + dark_yellow(string, end) + dark_blue(string, end) + dark_magenta(string, end) + dark_cyan(string, end) + dark_gray(string, end)
        else:
            raise TypeError
    else:
        raise TypeError


def light_rainbow(string="Hello, World!", end=True):
    """
    Creates a Rainbow of the Text in the String in the Light Colors

    :param string: Inputted String
    :param end: Adds the ANSI Escape Code for END to Make Text After It Normal
    :type string: str
    :type end: bool
    :return: Eights Strings of Eight Colors
    :rtype: str
    :raises TypeError: Incorrect Parameter Type Inputted"""

    if isinstance(string, str):
        if isinstance(end, bool):
            return light_gray(string, end) + red(string, end) + green(string, end) + yellow(string, end) + blue(string, end) + magenta(string, end) + cyan(string, end) + white(string, end)
        else:
            raise TypeError
    else:
        raise TypeError


def full_rainbow(string="Hello, World!", end=True):
    """
    Creates a Rainbow of the Text in the String in All of the Colors

    :param string: Inputted String
    :param end: Adds the ANSI Escape Code for END to Make Text After It Normal
    :type string: str
    :type end: bool
    :return: Sixteen Strings of Sixteen Colors
    :rtype: str
    :raises TypeError: Icorrect Parameter Type Inputted"""

    if isinstance(string, str):
        if isinstance(end, bool):
            return dark_rainbow(string, end) + light_rainbow(string, end)
        else:
            raise TypeError
    else:
        raise TypeError

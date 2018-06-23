##########
References
##########

Warning: Some Variables and Functions are NOT Cross-Platform

.. py:data:: END

    ANSI Escape Code to Change Text Back to Default

.. py:data:: BOLD

    ANSI Escape Code to Bold Text

.. py:data:: FAINT

    ANSI Escape Code to Lighten Text

.. py:data:: ITALIC

    ANSI Escape Code to Underline Text

.. py:data:: SLOWBLINK

    ANSI Escape Code to Slowly Bink Text

.. py:data:: RAPIDBLINK

    ANSI Escape Code to Rapidly Blink Text

.. py:data:: CROSSEDOUT

    ANSI Escape Code to Cross Out Text

.. py:data:: DEFAULT

    ANSI Escape Code to Change Font to Default

.. py:data:: FONTONE

    ANSI Escape Code to Change Font to Font One

.. py:data:: FONTTWO

    ANSI Escape Code to Change Font to Font Two

.. py:data:: FONTTHREE

    ANSI Escape Code to Change Font to Font Three

.. py:data:: FONTFOUR

    ANSI Escape Code to Change Font to Font Four

.. py:data:: FONTFIVE

    ANSI Escape Code to Change Font to Font Five

.. py:data:: FONTSIX

    ANSI Escape Code to Change Font to Font Six

.. py:data:: FONTSEVEN

    ANSI Escape Code to Change Font to Font Seven

.. py:data:: FONTEIGHT

    ANSI Escape Code to Change Font to Font Eight

.. py:function:: regular(string=None, end=True)

    Changes Text in Terminal to Default

    :param str string: Inputted String
    :param bool end: Adds the ANSI Escape Code for END to Make Text After the Escape Code Normal
    :return: ANSI Escape Code for END
    :rtype: str
    :raises TypeError: if the parameter string is not a string
    :raises TypeError: if the parameter end is not a boolean

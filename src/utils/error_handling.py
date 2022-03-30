import os
import string
import sys

PROCEED_WITH_DEFAULT = 'Do you wish to proceed with the default value?'
VALUE_OF = 'ValueError: The value of'


def query_yes_no(question, default="yes"):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
            It must be "yes" (the default), "no" or None (meaning
            an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True, "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and not choice:
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write(
                "Please respond with 'yes' or 'no' (or 'y' or 'n').\n")


def check_path(path: string, desc: string):
    try:
        if not path or not os.path.exists(path):
            raise FileNotFoundError(
                'FileNotFoundError: The path to the', desc, 'does not exist!')
    except FileNotFoundError as error:
        print(error)
        ans = query_yes_no(PROCEED_WITH_DEFAULT)
        if ans:
            return True
        else:
            sys.exit()


def check_bool(value: bool, name: string):
    try:
        if value == None:
            raise ValueError(
                'ValueError: The value of', name, ' needs to be either true or false!')
    except ValueError as error:
        print(error)
        ans = query_yes_no(PROCEED_WITH_DEFAULT)
        if ans:
            return True
        else:
            sys.exit()


def check_color(color_value: int, name: string):
    try:
        if color_value < 0 or color_value > 255:
            raise ValueError(
                VALUE_OF, name, ' needs to be between 0 and 255!')
    except ValueError as error:
        print(error)
        ans = query_yes_no(PROCEED_WITH_DEFAULT)
        if ans:
            return True
        else:
            sys.exit()


def check_percentage(percentage: float, name: string):
    try:
        if percentage < 0 or percentage > 1:
            raise ValueError(
                VALUE_OF, name, 'needs to be between 0 and 1!')
    except ValueError as error:
        print(error)
        ans = query_yes_no(PROCEED_WITH_DEFAULT)
        if ans:
            return True
        else:
            sys.exit()


def check_pos(pos: string, range: list):
    try:
        if not pos in range:
            raise ValueError(
                'ValueError: Position value is not one of the following accepted values:', range)
    except ValueError as error:
        print(error)
        ans = query_yes_no(PROCEED_WITH_DEFAULT)
        if ans:
            return True
        else:
            sys.exit()


def check_padding(padding: list[int, int]):
    try:
        if type(padding) != list or type(padding[0]) != int or type(padding[1]) != int:
            raise TypeError(
                'TypeError: Padding must either be specified as a float or an int list with length 2.')
    except ValueError as error:
        print(error)
        ans = query_yes_no(PROCEED_WITH_DEFAULT)
        if ans:
            return True
        else:
            sys.exit()

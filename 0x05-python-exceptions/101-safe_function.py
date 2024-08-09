#!/usr/bin/python3


import sys


def safe_function(fct, *args):
    """
    Executes a function safely and handles exceptions.

    Args:
        fct (function): The function to be executed.
        *args: Arguments to be passed to the function.

    Returns:
        Any: The result of the function if successful, None otherwise.
    """
    try:
        return fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
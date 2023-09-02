#!/usr/bin/env python3
"""Sandbox module.

"""

from collections import abc
from functools import singledispatch
from typing import Any, Sequence


@singledispatch
def is_sequence(value: Any) -> bool:
    """Evaluate whether given object is a valid sequence.

    Arguments:
        value: The object to evaluate.
    Returns:
        True if given object is a sequence.
        False otherwise.
    Raises:
        None.
    """
    return False


@is_sequence.register(abc.Sequence)
def _(value: Sequence) -> bool:
    return True


if __name__ == "__main__":
    import getpass
    import os

    opts = [
        os.getlogin,
        getpass.getuser,
        lambda: "anonymous",
    ]
    for fn in opts:
        try:
            user = fn()
        except Exception:
            continue  # not available for some reason

    print(f"Hello, {user}!", flush=True)

# __END__

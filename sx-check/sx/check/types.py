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
    import os

    print(f"Hello, {os.getlogin()}!", flush=True)

# __END__

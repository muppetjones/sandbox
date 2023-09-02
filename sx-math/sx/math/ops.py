#!/usr/bin/env python3
"""Dummy module for sandbox.

"""


import itertools
from typing import Any, Collection, Union


def add(*args: Union[Collection, int]) -> Any:
    """Add given arguments together.

    Arguments:
        *args: One or more accumulateable objects.
    Returns:
        Sum of given objects.
    Raises:
        TypeError if summation is not supported for given objects.
    """
    iterable = itertools.accumulate(args)
    return list(iterable)[-1]


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser()
    subparsers = parser.add_subparsers()

    parser_add = subparsers.add_parser("add")
    parser_add.add_argument("numbers", nargs="+", type=int)
    parser_add.set_defaults(func=lambda x: add(*x.numbers))

    args = parser.parse_args()
    result = args.func(args)
    print(result, flush=True)


# __END__

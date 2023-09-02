#!/usr/bin/env python3
""".

"""

import inspect
import logging
from collections import abc
from functools import singledispatch
from pprint import pformat
from typing import Any, Mapping, Optional


def inspect_object(
    value: Any, logger: Optional[logging.Logger] = None
) -> Mapping[str, Any]:
    """Inspect object's attributes."""
    logger = logger or logging.getLogger(__name__)
    info = dict(
        (attr, _inspect(getattr(value, attr), name=attr)) for attr in dir(value)
    )
    logger.debug(pformat(info))
    logger.critical(pformat(info))
    return info


@singledispatch
def _inspect(value: Any, name: str) -> Any:
    return value


@_inspect.register(str)
def _(value: str, name: str) -> str:
    return value


@_inspect.register(abc.Callable)
def _(value: str, name: str) -> inspect.Signature:
    return inspect.signature(value)


# __END__

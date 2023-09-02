#!/usr/bin/env python3
"""Test."""

import logging
import os
import shlex
import subprocess
from unittest import TestCase

import sx.check.types as MOD

LOGGER = logging.getLogger(__name__)


class ThisTestCase(TestCase):
    """Base test case for the module."""


class TestEntrypoint(ThisTestCase):
    """Test feature."""

    def test_greets_user(self) -> None:
        # Francis is curious and executes the module from the command line.

        module = MOD.__name__
        cmd = f"python3 -m {module} add 2 4 6"
        result = subprocess.run(shlex.split(cmd), capture_output=True, text=True)
        if 0 != result.returncode:
            LOGGER.info(result.stdout)
            LOGGER.error(result.stderr)
            result.check_returncode()

        # She is pleasantly surprised by the warm greeting!
        expected = f"Hello, {os.getlogin()}!"
        found = result.stdout.strip()
        self.assertEqual(expected, found)


# __END__

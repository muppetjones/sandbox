#!/usr/bin/env python3
"""Test."""

import logging
import shlex
import subprocess
from unittest import TestCase

import sx.math.ops as MOD

LOGGER = logging.getLogger(__name__)


class ThisTestCase(TestCase):
    """Base test case for the module."""


class TestOpsMain(ThisTestCase):
    """Test function."""

    def test_adds_numbers(self) -> None:
        # Brian wants to add some numbers, so he calls the sx function
        module = MOD.__name__
        cmd = f"python3 -m {module} add 2 4 6"
        result = subprocess.run(shlex.split(cmd), capture_output=True, text=True)
        if 0 != result.returncode:
            LOGGER.info(result.stdout)
            LOGGER.error(result.stderr)
            result.check_returncode()

        # And he sees the results printed to the console
        expected = "12"
        found = result.stdout.strip()
        self.assertEqual(expected, found)


# __END__

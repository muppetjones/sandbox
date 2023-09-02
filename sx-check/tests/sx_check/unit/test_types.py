#!/usr/bin/env python3
"""Test."""

import logging
from unittest import TestCase

import sx.check.types as MOD

LOGGER = logging.getLogger(__name__)


class ThisTestCase(TestCase):
    """Base test case for the module."""


class TestIsSequence(ThisTestCase):
    """Test function."""

    def test_returns_expected(self) -> None:
        tests = [
            # (expected, given)
            (True, "ab"),
            (True, list("ab")),
            (True, tuple("ab")),
            (False, set("ab")),
            (False, dict([("a", 1)])),
            (False, 0),
            (False, True),
            (False, self),
        ]
        for expected, given in tests:
            with self.subTest(given):
                found = MOD.is_sequence(given)
                self.assertEqual(expected, found)


# __END__

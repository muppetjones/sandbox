#!/usr/bin/env python3
"""Test."""

import logging
from unittest import TestCase

import sx.math.ops as MOD

LOGGER = logging.getLogger(__name__)


class ThisTestCase(TestCase):
    """Base test case for the module."""


class TestAdd(ThisTestCase):
    """Test function."""

    def test_raises_for_incompatible_input(self) -> None:
        with self.assertRaisesRegex(TypeError, "unsupported"):
            MOD.add(1, "a")

    def test_returns_expected_sum(self) -> None:
        tests = [
            # (expected, given)
            ("abc", list("abc")),
            (4, [1, 2, 1]),
            ((1, 2, 3), [(1, 2), (3,)]),
        ]
        for expected, given in tests:
            with self.subTest(given):
                found = MOD.add(*given)
                self.assertEqual(expected, found)


# __END__

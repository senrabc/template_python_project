# -*- coding: utf-8 -*-

from .context import {{ cookiecutter.project_slug }}

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_foo(self):
        self.assertIsNone({{ cookiecutter.project_slug }}.foo())


if __name__ == '__main__':
    unittest.main()

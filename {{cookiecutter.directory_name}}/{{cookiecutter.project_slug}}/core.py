# -*- coding: utf-8 -*-
from . import utils

def get_foo():
    """Get a foo."""
    return '...foo'


def foo():
    """foo..."""
    if utils.get_bar():
        print(get_foo())

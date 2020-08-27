#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains functions and classes related to MotionBuilder UI
"""

from __future__ import print_function, division, absolute_import

from tpDcc.libs.qt.core import qtutils


def get_mobu_window():
    """
    Return the MotionBuilder main window widget as a Python object
    :return: Maya Window
    """

    return qtutils.get_main_qt_window()

#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains DCC functionality for MotionBuilder
"""

from __future__ import print_function, division, absolute_import

from tpDcc.core import dcc
from tpDcc.dccs.mobu.core import helpers, gui


def get_name():
    """
    Returns the name of the DCC
    :return: str
    """

    return dcc.Dccs.MotionBuilder


def get_extensions():
    """
    Returns supported extensions of the DCC
    :return: list(str)
    """

    return ['.fbx']


def get_allowed_characters():
    """
    Returns regular expression of allowed characters in current DCC
    :return: str
    """

    return 'A-Za-z0-9_. /+*<>=|-'


def get_version():
    """
    Returns version of the DCC
    :return: int
    """

    return helpers.get_mobu_version()


def get_version_name():
    """
    Returns version of the DCC
    :return: str
    """

    return str(helpers.get_mobu_version())


def is_batch():
    """
    Returns whether DCC is being executed in batch mode or not
    :return: bool
    """

    return False


def enable_component_selection():
    """
    Enables DCC component selection mode
    """

    return False


def get_main_window():
    """
    Returns Qt object that references to the main DCC window
    :return:
    """

    return gui.get_mobu_window()


def get_main_menubar():
    """
    Returns Qt object that references to the main DCC menubar
    :return:
    """

    return None


def parent_widget_to_dcc_window(widget):
    """
    Parents given widget to main DCC window
    :param widget: QWidget
    """

    flags = widget.windowFlags()
    widget.setParent(get_main_window())
    widget.setWindowFlags(flags)

#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Initialization module for tpDcc.dccs.mobu
"""

from __future__ import print_function, division, absolute_import

import os
import inspect
import logging

import tpDcc.register as core_register
from tpDcc.dccs.mobu import register
from tpDcc.dccs.mobu.core import dcc

# =================================================================================

PACKAGE = 'tpDcc.dccs.mobu'

# =================================================================================


def get_module_path():
    """
    Returns path where tpDcc.dccs.mobu module is stored
    :return: str
    """

    try:
        mod_dir = os.path.dirname(inspect.getframeinfo(inspect.currentframe()).filename)
    except Exception:
        try:
            mod_dir = os.path.dirname(__file__)
        except Exception:
            try:
                import tpDcc.dccs.mobu
                mod_dir = tpDcc.dccs.mobu.__path__[0]
            except Exception:
                return None

    return mod_dir


def create_logger(dev=False):
    """
    Returns logger of current module
    """

    logger_directory = os.path.normpath(os.path.join(os.path.expanduser('~'), 'tpDcc', 'logs'))
    if not os.path.isdir(logger_directory):
        os.makedirs(logger_directory)

    logging_config = os.path.normpath(os.path.join(os.path.dirname(__file__), '__logging__.ini'))

    logging.config.fileConfig(logging_config, disable_existing_loggers=False)
    logger = logging.getLogger(PACKAGE.replace('.', '-'))
    if dev:
        logger.setLevel(logging.DEBUG)
        for handler in logger.handlers:
            handler.setLevel(logging.DEBUG)

    return logger


def init_dcc(dev=False):
    """
    Initializes module
    :param dev: bool, Whether to launch code in dev mode or not
    """

    if dev:
        register.cleanup()
        register_classes()

    register_resources()

    logger = create_logger(dev=dev)
    register.register_class('logger', logger)


def register_resources():
    """
    Registers tpDcc.libs.qt resources path
    """

    import tpDcc

    resources_manager = tpDcc.ResourcesMgr()
    resources_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resources')
    resources_manager.register_resource(resources_path, key=tpDcc.Dccs.Maya)


def register_classes():
    core_register.register_class('Dcc', dcc.MobuDcc)
    # core_register.register_class('DccProgressBar', dcc.MayaProgessBar)
    # core_register.register_class('Callbacks', callback.MayaCallback)
    # core_register.register_class('Menu', menu.MayaMenu)
    # core_register.register_class('Shelf', shelf.MayaShelf)
    # core_register.register_class('Completer', completer.MayaCompleter)
    # core_register.register_class('Dialog', dialog.MayaDialog)
    # core_register.register_class('OpenFileDialog', dialog.MayaOpenFileDialog)
    # core_register.register_class('SaveFileDialog', dialog.MayaSaveFileDialog)
    # core_register.register_class('SelectFolderDialog', dialog.MayaSelectFolderDialog)
    # core_register.register_class('NativeDialog', dialog.MayaNativeDialog)
    # core_register.register_class('Window', window.MayaWindow)
    # core_register.register_class('DockWindow', window.MayaWindow)
    # core_register.register_class('SubWindow', window.MayaWindow)


register_classes()

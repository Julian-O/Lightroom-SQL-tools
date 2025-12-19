# -*- coding: utf-8 -*-
# pylint: disable=invalid-name

"""

Configuration for LRTool

"""
import logging
import sys
import os
from configparser import ConfigParser

# config file
CONFIG_FILENAME = "lrtools.ini"
# sections
CONFIG_MAIN = "Main"


class LRConfigException(Exception):
    """lrtools config exception"""


class LRToolConfig:
    """
    Data structure for storing system-wide configs.

    Will load from a file, unless config_filename is None.
    Default config file is called "lrtools.ini" in the current directory.
    """

    def __init__(self, config_filename="lrtools.ini"):
        """load default config"""
        self.default_lrcat = (
            "C:\\Users\\Default\\Documents\\My Lightroom Catalog.lrcat"
        )
        self.dayfirst = True
        self.geocoder = "nominatim"

        if config_filename:
            try:
                self.load(config_filename)
            except LRConfigException as e:
                logging.getLogger("lrtools").warning(
                    "Failed to read config file %s: %s",
                    (config_filename, e)
                )

    def load(self, filename):
        """load a config file"""

        # parser and default value
        parser = ConfigParser(
            {
                "LRCatalog": self.default_lrcat,
                "DayFirst": self.dayfirst,
                "GeoCoder": self.geocoder,
            }
        )

        # config file is located in directory where main script is lauched
        _dir, _ = os.path.split(filename)
        if _dir:
            config_file = filename
        else:
            config_file = os.path.join(os.path.dirname(sys.argv[0]), filename)

        parser.read(config_file)
        try:
            self.default_lrcat = parser.get(CONFIG_MAIN, "LRCatalog")
            self.dayfirst = parser.get(CONFIG_MAIN, "DayFirst")
            self.geocoder = parser.get(CONFIG_MAIN, "GeoCoder")

        except Exception as _e:
            raise LRConfigException(
                f'Failed to read config file "{filename}"'
            ) from _e


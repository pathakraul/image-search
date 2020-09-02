# -*- coding: utf-8 -*-
import argparse
import sys
import logging
import numpy as np
import h5py
import os
import sys
import time
import matplotlib
from pathlib import Path
from PIL import Image
import imagehash
from lookuptable import *


__author__ = "Rahul Pathak"
__copyright__ = "Rahul Pathak"
__license__ = "mit"
__version__ = "0.1.0"

_logger = logging.getLogger(__name__)

HEIGHT = 1024    
WIDTH = 1024    
CHANNELS = 3
IMAGEFOLDER = "../data/images"    
LOOKUPTABLE = "../data/lookuptable.h5"

def parse_args(args):
    """Parse command line parameters

    Args:
      args ([str]): command line parameters as list of strings

    Returns:
      :obj:`argparse.Namespace`: command line parameters namespace
    """
    parser = argparse.ArgumentParser(
        description="Lookup table generator for Image Comparison")
    parser.add_argument(
        "--version",
        action="version",
        version="lookuptable {ver}".format(ver=__version__))
    parser.add_argument(
        "-f",
        "--folder",
        dest="imagefolder",
        help="path to image folder",
        type=str,
        metavar="STRING")
    parser.add_argument(
        "-v",
        "--verbose",
        dest="loglevel",
        help="set loglevel to INFO",
        action="store_const",
        const=logging.INFO)
    parser.add_argument(
        "-vv",
        "--very-verbose",
        dest="loglevel",
        help="set loglevel to DEBUG",
        action="store_const",
        const=logging.DEBUG)
    return parser.parse_args(args)


def setup_logging(loglevel):
    """Setup basic logging

    Args:
      loglevel (int): minimum loglevel for emitting messages
    """
    logformat = "[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
    logging.basicConfig(level=loglevel, stream=sys.stdout,
                        format=logformat, datefmt="%Y-%m-%d %H:%M:%S")



def getentry(imagename):
    pass
    # Need to implement

def getimagelist(folder):    
    """function to read folder and generate the list of image names
    
    Args:
        folder (str): path of the images 
    """
    imagefolder = Path(folder)    
    imagelist = imagefolder.glob("**/*.png")    
    return list(imagelist)    


def main(args):
    """Main entry point allowing external calls

    Args:
      args ([str]): command line parameter list
    """
    args = parse_args(args)
    setup_logging(args.loglevel)
    _logger.debug("Starting crazy calculations...")
    createlookuptable(args.imagefolder)
    _logger.info("Script ends here")


def run():
    """Entry point for console_scripts
    """
    main(sys.argv[1:])


if __name__ == "__main__":
    run()

"""check_env.py for IPython.parallel tutorial at SciPy 2014"""

import sys

import numpy
import scipy

import requests

import matplotlib.pyplot
import skimage

import matplotlib

try:
    from bs4 import BeautifulSoup
except ImportError:
    print("BeautifulSoup will be used for an example.")

try:
    import networkx
except ImportError:
    print("networkx will be used for an example.")

try:
    import cv
except ImportError:
    print("opencv will be used for an example.")

from distutils.version import LooseVersion as V
import IPython

if V(IPython.__version__) < V('2.0'):
    print("Need IPython >= 2.0, have %s" % IPython.__version__)
    sys.exit(1)

from IPython import parallel

print("OK")

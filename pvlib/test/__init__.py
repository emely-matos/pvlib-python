# the has/skip patterns closely follow the examples set by
# the xray/xarray project

import sys
import platform
import pandas as pd
import numpy as np


try:
    import unittest2 as unittest
except ImportError:
    import unittest


try:
    import scipy
    has_scipy = True
except ImportError:
    has_scipy = False


def requires_scipy(test):
    return test if has_scipy else unittest.skip('requires scipy')(test)


try:
    import ephem
    has_ephem = True
except ImportError:
    has_ephem = False


def requires_ephem(test):
    return test if has_ephem else unittest.skip('requires ephem')(test)


def incompatible_conda_linux_py3(test):
    """
    Test won't work in Python 3.x due to Anaconda issue.
    """
    major = sys.version_info[0]
    minor = sys.version_info[1]
    system = platform.system()

    if major == 3 and system == 'Linux':
        out = unittest.skip('error on Linux Python 3 due to Anaconda')(test)
    else:
        out = test

    return out


def incompatible_pandas_0131(test):
    """
    Test won't work on pandas 0.18.0 due to pandas/numpy issue with
    np.round.
    """

    if pd.__version__ == '0.13.1':
        out = unittest.skip(
            'error on pandas 0.13.1 due to pandas/numpy')(test)
    else:
        out = test

    return out


def needs_numpy_1_10(test):
    """
    Test won't work on numpy 1.10.
    """

    major = int(np.__version__.split('.')[0])
    minor = int(np.__version__.split('.')[1])

    if major == 1 and minor < 10:
        out = unittest.skip('needs numpy 1.10')(test)
    else:
        out = test

    return out

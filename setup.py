#! /usr/bin/env python
#
# Copyright (C) 2015-2016 Jacob Graving <jgraving@gmail.com>

import os
# temporarily redirect config directory to prevent matplotlib importing
# testing that for writeable directory which results in sandbox error in
# certain easy_install versions
os.environ["MPLCONFIGDIR"] = "."

DESCRIPTION = "tracktor: multi-object traking using OpenCV"
LONG_DESCRIPTION = """\
Tracktor is an OpenCV based object tracking software. The software is able to perform single-object tracking in noisy environments or
multi-object tracking in uniform environments while maintaining individual identities. The tool is aimed at teaching biologists the 
basics of computer vision while solving relatively easy tracking problems.
"""

DISTNAME = 'tracktor'
MAINTAINER = 'Vivek Hari Sridhar'
MAINTAINER_EMAIL = 'vivekhsridhar@yahoo.com'
URL = 'http://vhsridhar.wordpress.com'
LICENSE = 'MIT License'
DOWNLOAD_URL = 'https://github.com/vivekhsridhar/tracktor.git'
VERSION = '0.1'

try:
    from setuptools import setup
    _has_setuptools = True
except ImportError:
    from distutils.core import setup

def check_dependencies():
    install_requires = []

    # Make sure dependencies exist

    try:
        import numpy
    except ImportError:
        install_requires.append('numpy')
    try:
        import pandas
    except ImportError:
        install_requires.append('pandas')
    try:
        import scipy
    except ImportError:
        install_requires.append('scipy')
    try:
        import cv2
    except ImportError:
        raise ImportError('opencv not found! Install OpenCV separately before running tracktor')
    try:
        import sklearn
    except ImportError:
        install_requires.append('sklearn')

    return install_requires

if __name__ == "__main__":

    install_requires = check_dependencies()

    setup(name=DISTNAME,
        author=MAINTAINER,
        author_email=MAINTAINER_EMAIL,
        maintainer=MAINTAINER,
        maintainer_email=MAINTAINER_EMAIL,
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        license=LICENSE,
        url=URL,
        version=VERSION,
        download_url=DOWNLOAD_URL,
        install_requires=install_requires,
        packages=['pinpoint'],
        classifiers=[
                     'Intended Audience :: Science/Research',
                     'Programming Language :: Python :: 3',
                     'License :: MIT License',
                     'Topic :: Scientific/Engineering :: Visualization',
                     'Topic :: Scientific/Engineering :: Image Recognition',
                     'Topic :: Scientific/Engineering :: Information Analysis',
                     'Topic :: Multimedia :: Video'
                     'Operating System :: Windows'
                     'Operating System :: POSIX',
                     'Operating System :: Unix',
                     'Operating System :: MacOS'],
          )
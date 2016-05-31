# ----------------------------------------------------------------------------
# Copyright (c) 2013--, BP development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------
import os
from setuptools import setup
from setuptools.extension import Extension

import numpy as np

classes = """
    Development Status :: 4 - Beta
    License :: OSI Approved :: BSD License
    Topic :: Scientific/Engineering
    Programming Language :: Python
    Programming Language :: Python :: 3.4
    Programming Language :: Python :: 3.5
    Operating System :: Unix
    Operating System :: POSIX
    Operating System :: MacOS :: MacOS X
"""
classifiers = [s.strip() for s in classes.split('\n') if s]

long_description = """An implementation of a balanced tree as described by
Cordova and Navarro"""

USE_CYTHON = os.environ.get('USE_CYTHON', True)
ext = '.pyx' if USE_CYTHON else '.c'
extensions = [Extension("bp._bp",
                        ["bp/_bp" + ext]),
              Extension("bp._parse",
                        ["bp/_parse" + ext])]

if USE_CYTHON:
    from Cython.Build import cythonize
    extensions = cythonize(extensions)
setup(name='bp',
      version=0.1,
      description='Balanced parentheses',
      author='Daniel McDonald',
      author_email='mcdonadt@colorado.edu',
      maintainer='Daniel McDonald',
      maintainer_email='mcdonadt@colorado.edu',
      url='https://github.com/wasade/improved-octo-waddle',
      packages=['bp'],
      ext_modules=extensions,
      include_dirs=[np.get_include()],
      setup_requires=['numpy >= 1.9.2'],
      install_requires=[
          'numpy >= 1.9.2',
          'nose >= 1.3.7'],
      long_description=long_description)

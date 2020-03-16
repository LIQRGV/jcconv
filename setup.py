# -*- coding: utf-8 -*-
from setuptools import setup
import sys
import unittest

import jcconv3
from jcconv3 import __version__, __license__, __author__

if __name__ == '__main__':
  from jcconv3 import jcconv3_test
  # run module test
  loader = unittest.TestLoader()
  result = unittest.TestResult()
  suite  = loader.loadTestsFromModule(jcconv3_test)
  suite.run(result)
  if not result.wasSuccessful():
    print("unit tests have failed!")
    print("aborted to make a source distribution")
    sys.exit(1)

  # build distribution package
  setup(
    packages         = ('jcconv3',),
    name             = 'jcconv3',
    version          = __version__,
    py_modules       = ['jcconv3/jcconv3', 'jcconv3/jcconv3_test'],
    description      = 'jcconv "JapaneseCharacterCONVerter", interconvert hiragana, katakana, halfwidth kana',
    long_description = jcconv3.__doc__,
    author           = __author__,
    author_email     = 'taichino@gmail.com',
    url              = 'http://github.com/LIQRGV/jcconv',
    keywords         = 'japanese converter, hiragana, katakana, half-width kana',
    license          = __license__,
    classifiers      = ["Development Status :: 3 - Alpha",
                        "Intended Audience :: Developers",
                        "License :: OSI Approved :: MIT License",
                        "Operating System :: POSIX",
                        "Programming Language :: Python",
                        "Topic :: Software Development :: Libraries :: Python Modules"]
    )

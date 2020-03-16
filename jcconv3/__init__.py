#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
   jcconv, Japanese Characters CONVerter, interconvert hiragana, katakana, half-width kana.
   This module also treat 'half/wide number', 'half/wide alphabet'.

   Since 0.2.0, check_hira, check_kata, check_half functions were added.
   you can check if string consists of characters you specified.
   
   IMPOTANT: In current version, this works only with utf-8 encoding.


   Simple example of usage is followings

       >>> from jcconv3 import *
       >>> print(hira2kata('あいうえお'))   # hiragana to katakana
       アイウエオ
       >>> print(kata2hira('カタカナ'))     # katakana to hiragana
       かたかな
       >>> print(half2hira('ﾊﾝｶｸｶﾀｶﾅ'))      # half-width kana to hiragana
       はんかくかたかな
       >>> print(half2wide('hello jcconv')) # half-width alphabet to wide-width
       ｈｅｌｌｏ ｊｃｃｏｎｖ
       >>> print(wide2half('ＷＩＤＥ'))     # wide-width alphabet to half-width
       WIDE
"""

__author__  = ["Septian Hari", "Matsumoto Taichi"]
__version__ = "1.2.3"
__license__ = "MIT License"

from .jcconv3 import *

__all__ = ['hira2kata', 'kata2hira', 'half2hira', 'hira2half', 'kata2half',
           'half2kata', 'half2wide', 'wide2half', 'convert',
           'check_hira', 'check_kata', 'check_half']

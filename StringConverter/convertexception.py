# !/usr/bin/python
# -*- coding: utf-8 -*-


"""
author  : Bilery Zoo(652645572@qq.com)
time    : 2018-05-24
program : *_* Exception definition of convert function *_*
"""


class ConvertException(Exception):
    pass


class InvalidStringsException(ConvertException):
    def __str__(self):
        print('o(>﹏<)o Get invalid string(s) only "\033[1;31;40mALPHABET & SPACE\033[0m" are allowed o(>﹏<)o')


class LineHeadException(ConvertException):
    def __str__(self):
        print('o(>﹏<)o "\033[1;31;40mBLANKS\033[0m" at the beginning of line is forbidden o(>﹏<)o')


class LineTailException(ConvertException):
    def __str__(self):
        print('o(>﹏<)o "\033[1;31;40mBLANKS\033[0m" at the end of line is forbidden o(>﹏<)o')


class DuplicateBlanksException(ConvertException):
    def __str__(self):
        print('o(>﹏<)o Between word and word only "\033[1;31;40mONE BLANK\033[0m" is allowed o(>﹏<)o')
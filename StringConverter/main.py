# !/usr/bin/python
# -*- coding: utf-8 -*-


"""
author  : Bilery Zoo(652645572@qq.com)
time    : 2018-05-24
program : *_* Main call *_*
"""


import time
import convert
import convertexception


while True:
    try:
        strings = raw_input("Please input (Ctrl-C to exit):\n")
        if strings:
            print(convert.convert(strings))
    except convertexception.ConvertException as E:
        print(E.__str__())
        continue
    except Exception as E:
        print(E)
        break
    except KeyboardInterrupt:
        print("\nGoodbye at {ts}. See you...".format(ts=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
        break
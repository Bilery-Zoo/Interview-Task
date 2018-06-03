# !/usr/bin/python
# -*- coding: utf-8 -*-


"""
author  : Bilery Zoo(652645572@qq.com)
time    : 2018-05-24
program : *_* String convert handler *_*
"""


import convertexception


def convert(strings):
    """
    Convert strings inputted with each word spelled in reverse and case sensitive remained.Strings:
        ①contain only alphabet (a-z and A-Z) and space
        ②each word separated by exactly one space
        ③no spaces before or after the line
    :param strings: string
        Strings inputted.
    :return: string
        Strings with each inputted word spelled in reverse and case sensitive remained.
    """

    if not strings.replace(' ', '').isalpha():
        raise convertexception.InvalidStringsException
    elif strings[0].isspace():
        raise convertexception.LineHeadException
    elif strings[-1].isspace():
        raise convertexception.LineTailException
    else:
        for i in range(len(strings)):
            if strings[i] == ' ' == (strings[1:] + ' ')[i]:
                raise convertexception.DuplicateBlanksException

    stringswords = strings.split()
    convertwords = []
    for word in stringswords:
        wordletters = list(word)
        wordletterscases = []
        for letter in wordletters:
            wordletterscases.append(letter.isupper())
        wordletters.reverse()
        for i in range(len(wordletters)):
            if wordletterscases[i]:
                wordletters[i] = wordletters[i].upper()
            elif not wordletterscases[i]:
                wordletters[i] = wordletters[i].lower()
        convertwords.append(''.join(wordletters))

    return ' '.join(convertwords)


if __name__ == "__main__":
    s = "Many people spell MySQL incorrectly"
    print(s)
    print(convert(s))
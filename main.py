#!/usr/bin/env python
# -*- coding: utf-8 -*-

import saynumberinwords

def main():
    sp = saynumberinwords.supported_languages
    print ("The supported languages are：")
    for lan in sp:
        print (lan)

    nt = saynumberinwords.SayNumberInWords.setlanguage("Chinese")
    answer = nt.speak("123.5")
    print (answer)

if __name__ == '__main__':
    main()

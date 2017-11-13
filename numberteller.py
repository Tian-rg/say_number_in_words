#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''This module is intended to transfer number into words in different 
languages.
'''

__author__ = "Tian"

import multilinguisticspeaker as mls

class NumberTeller:
    '''say the number in Chinese.
    '''
    
    def __init__(self, language=None):
        self.languages = list(mls.supported_languages.keys())
        if not language:
            self.language = self.languages[0]
        else:
            self.__checklanguage(language.capitalize())
            self.language = language.capitalize()
    
    def setlanguage(self, language=None):
        self.__checklanguage(language.capitalize())
        if language==None:
            self.language = self.languages[0]
        self.language = language.capitalize()
    
    def say(self, number):
       
        in1 = ""
        in2 = ""
        
        try:
            return mls.supported_languages[self.language](number)
        except mls.NotCorrectNumberError:
            return "I caught mls.NotCorrectNumberError!\n"
        else:
            pass
        finally:
            pass

    def __checklanguage(self, language):
        '''Check if the language you want is supported!
        '''
    
        if not language.capitalize() in mls.supported_languages.keys():
            raise LanguageNotSupportedError('Do not support the language you want')
        else:
            pass
    
#    def __checknumber(self, number):
#       
#        number1 = str(number).split(".")[0]
#        if number1=="":
#            number1 = "0"
#       
#        if len(number1) > mls.supported_number_length[0]:
#            raise NumberTooLargeError("Number is too large to handle")
#        
#        if len(str(number).split(".")) == 2:
#            number2 = str(number).split(".")[1]
#            if len(number2) > mls.supported_number_length[1]:
#                raise TooManyDecimalDigits("Too many decimal digits to handle")
#        
#        if str(number).count(".")>=2:
#            raise NotCorrectNumberError("Wrong number format")
#        elif (len(number1)>1) and (number1.startswith('0')):
#            raise NotCorrectNumberError("Wrong number format")
#        elif not number1.isnumeric():
#            raise NotCorrectNumberError("Wrong number format")

class LanguageNotSupportedError(Exception):
    pass

#class NotCorrectNumberError(Exception):
#    pass

#class NumberTooLargeError(Exception):
#    pass

#class TooManyDecimalDigits(Exception):
#    pass
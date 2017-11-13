#!/usr/bin/env python
# -*- coding: utf-8 -*-

class NumberTeller(object):

	@classmethod
	def set_language(cls, language):	
		for sub_cls in cls.__subclasses__():
			if language == sub_cls.__name__:
				return sub_cls()

	def speak():
		pass

class Chinese(NumberTeller):

	def speak(self):
		return "Speak in Chinese!"

class Indonesian(NumberTeller):

	def speak(self):
		return "Speak in Indoensian!"

def main():
	nt = NumberTeller.set_language("Indonesian")
	answer = nt.speak()
	print (answer)

if __name__ == '__main__':
	main()

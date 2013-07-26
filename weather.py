#!/usr/bin/python2

class Weather(object):
	def __init__(self, temperature):
		self.temp = temperature

	def activate(self):
		print "It's now {} degrees Celsius.".format(self.temp)

class Cool(Weather):
	def __init__(self):
		self.temp = 19.0

class Moderate(Weather):
	def __init__(self):
		self.temp = 25.0

class Hot(Weather):
	def __init__(self):
		self.temp = 30.0

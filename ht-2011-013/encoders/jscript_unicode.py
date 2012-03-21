#! /usr/bin/env python

#Copyright HT srl, 2009-2010
#http://www.hackingteam.it/ for more information

#cod

"""
jscript_unicode encoders
Transform an input array in unicode format (padding with 90h)

"""

VERSION = "1.0"

NAME="jscript_unicode"
DESCRIPTION="jscript unicode converter"
DOCUMENTATION={}
DOCUMENTATION["VENDOR"] = "HT srl"
DOCUMENTATION["Repeatability"] = "not applicable"
DOCUMENTATION["Author"] = "cod"
DOCUMENTATION["Notes"] = ""

import os
import sys

class jscript_unicode:

	useBigEndian = True
	
	"""
	ctor
	"""
	def __init__(self):
		self.useBigEndian = True
	
	def switch(self):
		self.useBigEndian = not self.useBigEndian
		
	def get_little_endian(self, data):
		value = ""
		
		shellCodeEven = len(data)
		
		if (shellCodeEven % 2) != 0:
			shellCodeEven = shellCodeEven - 1
			
		i = 0
		
		while i < shellCodeEven:
			b0 = ord(data[i]) # .replace("\\x", "")
			b1 = ord(data[i+1]) # .replace("\\x", "")
			#exec 'ar = u"\\u%02x%02x"' % (b0, b1)
		
			b0 = hex(b0).replace("0x", "")
			if len(b0) < 2:
				b0 = '0' + b0

			b1 = hex(b1).replace("0x", "")
			if len(b1) < 2:
				b1 = '0' + b1

			value += "%u" + b0 + b1
			i += 2
        
		if (len(data) % 2) != 0:
			b0 = 0x90
			b1 = ord(data[i])

			b0 = hex(b0).replace("0x", "")
			if len(b0) < 2:
				b0 = '0' + b0

			b1 = hex(b1).replace("0x", "")
			if len(b1) < 2:
				b1 = '0' + b1

			value += "%u" + b0 + b1
		
		return value

	def get_big_endian(self, data):
		value = ""
		
		shellCodeEven = len(data)
		
		if (shellCodeEven % 2) != 0:
			shellCodeEven = shellCodeEven - 1
			
		i = 0
		
		while i < shellCodeEven:
			b0 = ord(data[i+1]) # .replace("\\x", "")
			b1 = ord(data[i]) # .replace("\\x", "")
			#exec 'ar = u"\\u%02x%02x"' % (b0, b1)
		
			b0 = hex(b0).replace("0x", "")
			if len(b0) < 2:
				b0 = '0' + b0

			b1 = hex(b1).replace("0x", "")
			if len(b1) < 2:
				b1 = '0' + b1

			value += "%u" + b0 + b1
			i += 2
        
		if (len(data) % 2) != 0:
			b0 = 0x90
			b1 = ord(data[i])

			b0 = hex(b0).replace("0x", "")
			if len(b0) < 2:
				b0 = '0' + b0

			b1 = hex(b1).replace("0x", "")
			if len(b1) < 2:
				b1 = '0' + b1

			value += "%u" + b0 + b1
		
		return value

	def get(self, data):
		if self.useBigEndian == True:
			value = self.get_big_endian(data)
		else:
			value = self.get_little_endian(data)
		
		return value

	def get2(self, data, prefix):
		if self.useBigEndian == True:
			value = self.get_big_endian(data)
		else:
			value = self.get_little_endian(data)
		
		return value.replace("%u", prefix)

		
if __name__ == "__main__":
	print "jscript/unicode adapter"
	
	print "Getting input file"
	
	myclass = jscript_unicode()
	
	print "Opening file ", sys.argv[1]
	
	fd = open(sys.argv[1], "rb")
	
	array = fd.read()
	
	outdata = myclass.get(array)
	
	fd.close()
	#report
	fd = open(sys.argv[2], "wb")

	fd.write(outdata)
	fd.close()

	print "Transform completed"

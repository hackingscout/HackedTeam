#! /usr/bin/env python

#Copyright HT srl, 2009-2010
#http://www.hackingteam.it/ for more information

#cod

"""
hex encoders
Transform an input array in hex arrays (??)

"""

VERSION = "1.0"

NAME="hex_encoders"
DESCRIPTION="hex_encoders converter"
DOCUMENTATION={}
DOCUMENTATION["VENDOR"] = "HT srl"
DOCUMENTATION["Repeatability"] = "not applicable"
DOCUMENTATION["Author"] = "cod"
DOCUMENTATION["Notes"] = ""

import os
import sys

class hex_encoders:

	"""
	ctor
	"""

	def get(self, data):
		value = ""
		size = len(data)
		
		padding = 0
		i = 0
		
		while i < size:
			
			b0 = ord(data[i])
			b0 = hex(b0)

			if len(b0) < 2:
				b0 = '0' + b0

			value += b0
			i += 1
			padding += 1

		return value
		
if __name__ == "__main__":
	print "hex/ encoder"
	
	print "Getting input file"
	
	myclass = hex_encoders()
	
	print "Opening file ", sys.argv[1]
	
	fd = open(sys.argv[1], "rb")
	
	array = fd.read()
	
	outdata = myclass.get(array)
	
	#report
	print outdata
	
	print "Transform completed"

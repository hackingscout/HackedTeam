#! /usr/bin/env python

#Copyright HT srl, 2009-2010
#http://www.hackingteam.it/ for more information

#cod

"""
c_array encoders
Transform an input array in c arrays (char array[size] = { data };

"""

VERSION = "1.0"

NAME="c_array"
DESCRIPTION="c_array converter"
DOCUMENTATION={}
DOCUMENTATION["VENDOR"] = "HT srl"
DOCUMENTATION["Repeatability"] = "not applicable"
DOCUMENTATION["Author"] = "cod"
DOCUMENTATION["Notes"] = ""

import os
import sys

class c_array:

	"""
	ctor
	"""

	def get(self, data):
		value = ""
		size = len(data)
		
		padding = 0
		i = 0
		
		value = "char array[%d] = {"%(size)
		
		while i < size:
			if (padding == 0):
				value += "\n\t"
			
			b0 = ord(data[i])
			b0 = hex(b0).replace("0x", "").upper()

			if len(b0) < 2:
				b0 = '0' + b0

			value += "0x" + b0
			i += 1
			padding += 1

			if (i != (size-1)):
				value += ", "
		
			if (padding == 16):
				padding = 0

		value += "\n};"
		
		return value
		
if __name__ == "__main__":
	print "vba/ encoder"
	
	print "Getting input file"
	
	myclass = c_array()
	
	print "Opening file ", sys.argv[1]
	
	fd = open(sys.argv[1], "rb")
	
	array = fd.read()
	
	outdata = myclass.get(array)
	
	#report
	print outdata
	
	print "Transform completed"

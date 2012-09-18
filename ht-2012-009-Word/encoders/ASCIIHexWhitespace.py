#! /usr/bin/env python

#Copyright HT srl, 2009-2010
#http://www.hackingteam.it/ for more information

#cod

"""
ASCII Hex Whitespace Encoder
Encode an array in ascii hex with space

"""

VERSION = "1.0"

NAME="ASCIIHexWhitespace"
DESCRIPTION="ASCIIHexWhitespace"
DOCUMENTATION={}
DOCUMENTATION["VENDOR"] = "HT srl"
DOCUMENTATION["Repeatability"] = "not applicable"
DOCUMENTATION["Author"] = "cod"
DOCUMENTATION["Notes"] = ""

import os
import sys

class ASCIIHexWhitespace:

	"""
	ctor
	"""

	def hexpad(self, byte):
		result = hex(byte).replace("0x", "")
		if len(result) < 2:
			result = "0" + result
		
		return result

	def get(self, data):
		value = ""
		whitespace = " "
		
		for i in range(len(data)):
			result = result + whitespace + hexpad(data[i])
		
		return value
		
if __name__ == "__main__":
	print "ASCIIHexWhitespace adapter"
	
	print "Getting input file"
	
	myclass = ASCIIHexWhitespace()
	
	print "Opening file ", sys.argv[1]
	
	fd = open(sys.argv[1], "rb")
	
	array = fd.read()
	
	outdata = myclass.get(array)
	
	#report
	print outdata
	
	print "Transform completed"

#! /usr/bin/env python

#Copyright HT srl, 2010
#http://www.hackingteam.it/ for more information

#cod

"""
Return a block of nop
"""

VERSION = "1.0"

NAME="x86nop"
DESCRIPTION="nop x86 generator"
DOCUMENTATION={}
DOCUMENTATION["VENDOR"] = "HT srl"
DOCUMENTATION["Repeatability"] = ""
DOCUMENTATION["Author"] = "cod"
DOCUMENTATION["Notes"] = "Return a block of nop"

import os
import sys

class x86nop:

	"""
	initialize object (shellcode)
	"""
	
	def __init__(self):
		return
	
	def get(self, size = 1):
		step = "\x90"
		
		i=0;
		shellcode = ""
		
		while(i < size):
			shellcode += step
			i += 1;
		
		return shellcode

if __name__ == "__main__":
	print DESCRIPTION
	
	print "Writing output in file 1"
	
	myclass = x86nop()
	
	print "Opening file ", sys.argv[1]
	
	size = 1
	
	if len(sys.argv) > 2:
		size = int(sys.argv[2])
		print "New size %d"%(size)
		
	outstream = open(sys.argv[1], 'wb')
	outstream.write(myclass.get(size))
	outstream.close()
	
	print "Process completed"
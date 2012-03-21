#! /usr/bin/env python

#Copyright HT srl, 2010
#http://www.hackingteam.it/ for more information

#cod

"""
Return a single breakpoint
"""

VERSION = "1.0"

NAME="x86int3"
DESCRIPTION=" x86 int3"
DOCUMENTATION={}
DOCUMENTATION["VENDOR"] = "HT srl"
DOCUMENTATION["Repeatability"] = ""
DOCUMENTATION["Author"] = "cod"
DOCUMENTATION["Notes"] = "Return a single breakpoint (for debugger, int 03/cc opcode)"

import os
import sys

class x86int3:

	"""
	initialize object ()
	"""
	
	def __init__(self):
		return
	
	def get(self):
		step = "\xcc"
		return step

if __name__ == "__main__":
	print DESCRIPTION
	
	print "Writing output in file 1"
	
	myclass = x86int3()
	
	print "Opening file ", sys.argv[1]
	
	size = 1
	
	if len(sys.argv) > 2:
		size = int(sys.argv[2])
		print "New size %d"%(size)
		
	outstream = open(sys.argv[1], 'wb')
	outstream.write(myclass.get(size))
	outstream.close()
	
	print "Process completed"
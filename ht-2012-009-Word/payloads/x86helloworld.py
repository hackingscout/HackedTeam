#! /usr/bin/env python

#Copyright HT srl, 2009-2010
#http://www.hackingteam.it/ for more information

#cod

"""
Simple hello world.. smallest version
"""

VERSION = "1.0"

NAME="x86helloworld"
DESCRIPTION="x86 Hello world! for win32"
DOCUMENTATION={}
DOCUMENTATION["VENDOR"] = "HT srl"
DOCUMENTATION["Repeatability"] = "One shot"
DOCUMENTATION["Author"] = "cod"
DOCUMENTATION["Notes"] = ""

import os
import sys
import struct
from random import *

class x86helloworld:

	shellcode = ""
	
	"""
	initialize object (shellcode and Random object)
	"""
	def __init__(self):

		self.shellcode += "\xE8\xFF\xFF\xFF\xFF\xC8\x58\x83\xC0\xF4\xEB\x23\x51\x56\x68\x64"
		self.shellcode += "\x64\x72\x65\x68\x72\x6F\x63\x41\x68\x47\x65\x74\x50\x8B\xF4\x33"
		self.shellcode += "\xC9\x83\xC9\x03\xF3\xA7\x0F\x94\xC0\x83\xC4\x0C\x5E\x59\xC3\xEB"
		self.shellcode += "\x53\x55\x8B\xEC\x56\x51\x57\x8B\x75\x0C\x8B\x4E\x18\x8B\x7E\x1C"
		self.shellcode += "\x03\x7D\x08\x8B\x46\x20\x03\x45\x08\x57\x50\x8B\x38\x03\x7D\x08"
		self.shellcode += "\xE8\xB7\xFF\xFF\xFF\x3C\x01\x58\x5F\x74\x0A\x83\xC7\x04\x83\xC0"
		self.shellcode += "\x04\xE2\xE6\xEB\x09\x8B\x3F\x03\x7D\x08\x8B\xC7\xEB\x0D\x33\xC0"
		self.shellcode += "\x8B\xFC\x33\xC9\x83\xC9\x40\xF3\xAB\xFF\xE0\x5F\x59\x5E\x8B\xE5"
		self.shellcode += "\x5D\xC2\x08\x00\xEB\x47\xFF\x65\xE0\xFF\x65\xDC\xFF\x65\xD8\x4D"
		self.shellcode += "\x65\x73\x73\x61\x67\x65\x42\x6F\x78\x41\x00\x45\x78\x69\x74\x50"
		self.shellcode += "\x72\x6F\x63\x65\x73\x73\x00\x48\x65\x6C\x6C\x6F\x20\x77\x6F\x72"
		self.shellcode += "\x6C\x64\x21\x00\x45\x78\x70\x6C\x6F\x69\x74\x20\x72\x75\x6E\x21"
		self.shellcode += "\x00\x8F\x00\xDC\xFF\xFF\xFF\x9B\x00\xD8\xFF\xFF\xFF\x8B\xEC\x83"
		self.shellcode += "\xEC\x40\x89\x45\xFC\x66\xB8\x30\x00\x66\x99\x64\x8B\x00\x8B\x40"
		self.shellcode += "\x0C\x8B\x70\x1C\xAD\x8B\x40\x08\x89\x45\xF8\x8B\x48\x3C\x03\xC8"
		self.shellcode += "\x8B\x49\x78\x03\xC8\x51\xFF\x75\xF8\xE8\x33\xFF\xFF\xFF\x89\x45"
		self.shellcode += "\xF4\x8B\x5D\xFC\x89\x45\xE0\xBB\xC1\x00\x00\x00\x03\x5D\xFC\x8B"
		self.shellcode += "\xF3\x33\xC9\xB1\x02\x51\x0F\xB7\x06\x46\x46\x03\x45\xFC\x50\xFF"
		self.shellcode += "\x75\xF8\xE8\x5F\xFF\xFF\xFF\x59\x8B\xD8\xAD\x03\xC5\x89\x18\xE2"
		self.shellcode += "\xE4\x6A\x10\x66\xBB\xB4\x00\x66\x99\x03\x5D\xFC\x53\x66\xBB\xA7"
		self.shellcode += "\x00\x66\x99\x03\x5D\xFC\x53\x6A\x00\xE8\x3B\xFF\xFF\xFF\x6A\x00"
		self.shellcode += "\xE8\x37\xFF\xFF\xFF"
	
	"""
	attach a file to shellcode and return an array (binary string)
	"""
	def get(self):
		outshellcode = self.shellcode

		return outshellcode
		
if __name__ == "__main__":
	print "x86 Hello world/win32 platform"
	
	print "Loading file 1"
	
	myclass = x86helloworld()
	
	print "Opening file ", sys.argv[1]
	outdata = myclass.get(sys.argv[1])
	
	outstream = open(sys.argv[2], 'wb')
	outstream.write(outdata)
	outstream.close()
	
	print "Block completed"

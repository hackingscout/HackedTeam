#! /usr/bin/env python

#Copyright HT srl, 2012
#http://www.hackingteam.it/ for more information

#cod

#
# build.py

import os
import sys
import warnings
import zipfile

def processdirectory(root_dir, dir_name, zip):

	for fn in os.listdir(dir_name):
		dirfile = os.path.join(dir_name, fn)
		if os.path.isdir(dirfile):
			print "Directory %s" % dirfile
			processdirectory(root_dir + "\\" + fn, os.path.join(dir_name, fn), zip)
		else:
			print "File %s" %dirfile
			zip.write(os.path.join(dir_name, fn), root_dir + "\\" + fn)

if __name__=='__main__':
	print 'Processing current directory...'
	
	for fn in os.listdir('.'):
		if os.path.isdir(fn):
			outFileName = fn[0:11] + '.zip'
			
			if os.path.isfile(outFileName):
				os.unlink(outFileName)
			
			print "Creating %s zip file archive"%(outFileName)
			zip = zipfile.ZipFile(outFileName, "w", zipfile.ZIP_DEFLATED)
			
			processdirectory("", fn, zip)
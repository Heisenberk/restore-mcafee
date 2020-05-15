#!/usr/bin/python3

import argparse
import sys
import os.path

# Parsing arguments
parser = argparse.ArgumentParser(description="Restore macafee files")
parser.add_argument('-i', action="store", dest="input")
parser.add_argument('-o', action="store", dest="output")
words = parser.parse_args(sys.argv[1:])

if words.input == None:
	print("Usage : ./restore-macafee.py -i [inputfile] -o [outputfile]")
	exit(1)
if os.path.exists(words.input) == False:
	print("Input File does not exist")
	exit(1)
if words.output == None:
	print("Usage : ./restore-macafee.py -i [inputfile] -o [outputfile]")
	exit(1)

# Restoration of the input file
input_file = open(words.input, "rb")
result_file = open(words.output, "wb")
key = 0x6a
byte = input_file.read(1)
while byte:
	result = int.from_bytes(byte, byteorder='big')^key
	result_file.write(result.to_bytes(1,'big'))
	byte = input_file.read(1)

input_file.close()
result_file.close()

print("[+] Restoration file done")


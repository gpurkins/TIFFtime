#!/usr/bin/python
# tiffdump.py - dumps time stamps from a Metamorph generated TIFF file.
# George Purkins - Aug 4, 2010
 
# Requires Python Image Library
import Image, re, optparse, sys

# Whatever... 
from optparse import OptionParser
parser = OptionParser()
(options, args) = parser.parse_args()

if (len(args) == 0):
	print "Needs at least one argument."
	exit()

if(len(args) > 2):
	print "Too many arguments.\n Usage: timestamps.py <input> <output>"
	print "Input is a TIFF stack, output is each frame's timestamp."
	exit()

im = Image.open(args[0]) 

im.seek(0) # Seek to beginning

if (len(args) == 2):
	fileopen = str(args[1])
else:
	fileopen = "timeStamps.txt"
	print "Default output to timeStamps.txt..."

fileout = open(fileopen, 'w')
fileout.write("Timestamps for: " + str(args[0]) + "\n")

try:
	while 1:
		# Grab time stamp from TIFF tag 306
		stamp = im.ifd.tagdata.get(306)
		# Search for everything between single quotes
		# Tag is a tuple: (2, '20100713 16:49:20.690\x00')
		stamp = re.search('\'.*\'', str(stamp))
		# Strip single quotes
		stamp = stamp.group(0).strip("'")
		# Break off end with null
		stamp = stamp.split("\\")
		# Stringify first element of list
		stamp = str(stamp[0])
		# Get found 
		#print stamp.group(0)
		fileout.write(stamp+"\n") # blarg out stamp
		im.seek(im.tell()+1) # seek to next image
except EOFError:
	pass # end of tifflist
	

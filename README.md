TIFFTime
=============
[TIFFTime] is an open source python tool that dumps time stamps from Metamorph generated TIFFs. These time stamps are generally at the thousandth second resolution. My old lab needed this in order to have more precise calculations for a curve.

Requirements
-------------

TIFFTime.py will only work if you have the Python Image Library installed. http://www.pythonware.com/products/pil/

Basics of Use
-------------

This should work on two color TIFFs from any Metamorph system. The results are delivered in a tuple '20100713 16:49:20.690', which is date and time. This should work for N colors, provided you split them based on the number of wavelengths.

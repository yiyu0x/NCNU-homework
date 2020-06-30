import struct

if struct.pack('@h', 1) == struct.pack('<h', 1):
	print('Little Endian')
else:
	print('Big-Endian')
import struct as s
import sys

if len(sys.argv) == 1:
	print('Please use "python app.py <file name>"')
	exit()

f = open(sys.argv[1], "rb")

print("{:>19s}".format('Format:'), '\'bmp\'')
print("{:>19s}".format('FormatSignature:'), f'\'{f.read(2).decode()}\'')
print("{:>19s}".format('FileSize:'), s.unpack("I", f.read(4))[0])

f.seek(2, 1) # keep bytes
f.seek(2, 1) # keep bytes

print("{:>19s}".format('ImageDataOffset:'), s.unpack("I", f.read(4))[0])
print("{:>19s}".format('BitmapHeaderSize:'), s.unpack("I", f.read(4))[0])
print("{:>19s}".format('Width:'), s.unpack("I", f.read(4))[0])
print("{:>19s}".format('height:'), s.unpack("I", f.read(4))[0])
print("{:>19s}".format('NumPlanes:'), s.unpack("h", f.read(2))[0])
print("{:>19s}".format('BitDepth:'), s.unpack("h", f.read(2))[0])

compression_type = s.unpack("I", f.read(4))[0]
com_type = ''
if compression_type == 0:
	com_type = 'none (0:BI_RGB)'
elif compression_type == 1:
	com_type = 'RLE 8-bit/pixel (1:BI_RLE8)'
elif compression_type == 2:
	com_type = 'RLE 4-bit/pixel (2:BI_RLE4)'
elif compression_type == 3:
	com_type = 'OS22XBITMAPHEADER: Huffman 1D(3:BI_BITFIELDS )'
elif compression_type == 4:
	com_type = 'OS22XBITMAPHEADER: RLE-24 (4:BI_JPEG)'
elif compression_type == 5:
	com_type = '(5:BI_PNG)'
elif compression_type == 6:
	com_type = 'RGBA bit field masks (6:BI_ALPHABITFIELDS)'
elif compression_type == 11:
	com_type = 'none ( 	BI_CMYK )'
elif compression_type == 12:
	com_type = 'RLE-8 BI_CMYKRLE8'
elif compression_type == 13:
	com_type = 'RLE-4 BI_CMYKRLE4'
print("{:>19s}".format('CompressionType:'), com_type)

print("{:>19s}".format('BitmapSize:'), s.unpack("I", f.read(4))[0])
print("{:>19s}".format('HorzResolution:'), s.unpack("I", f.read(4))[0])
print("{:>19s}".format('VertResolution:'), s.unpack("I", f.read(4))[0])
print("{:>19s}".format('NumColorsUsed:'), s.unpack("I", f.read(4))[0])
print("{:>19s}".format('NumImportantColors:'), s.unpack("I", f.read(4))[0])

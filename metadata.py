#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from tifffile import TiffFile
from struct import unpack

if len(sys.argv) < 2:
  print "Specify files via commandline - e.g., 'python metadata.py file1.tif file2.tif'"
  exit(1)

for file in sys.argv[1:]:
  print 'File: {}. Metadata found:'.format(file)
  with TiffFile(file) as tif:
    for page in tif:
      tag = page.tags['37554']
      b = tag.value
      print 'User: {}'.format(b[202:210])
      print 'Camera Model Number: {}'.format(b[237:242])
      print 'Serial Number: {}'.format(b[245:252])
      print 'Software Version: {}.{}.{}.{}'.format(unpack('b', b[214])[0], 0, unpack('b', b[226])[0], unpack('>H', b[231:233])[0])
      print u'Sensor Pixel Size: {} x {} µm'.format(unpack('>i', b[10:14])[0]/1000.0, unpack('>i', b[14:18])[0]/1000.0)
      print
      print 'Image Setup: {}'.format(b[190:199])
      print 'Exposure: {} ms'.format(unpack('>I',b[70:74])[0]/1000000.0)
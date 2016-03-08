#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from tifffile import TiffFile
from struct import unpack

if len(sys.argv) < 2:
  print "Specify files via commandline - e.g., 'python metadata.py file1.tif file2.tif'"
  exit(1)

print 'Filename, Exposure, Gain, Sensor Temperature'

for file in sys.argv[1:]:
  with TiffFile(file) as tif:
    for page in tif:
      tag = page.tags['37554']
      b = tag.value
      exposure = unpack('>Q',b[66:74])[0]/1000000.0
      gain = b[255:257]
      sens_temp = unpack('>h', b[95:97])[0]/10.0

      print '{}, {}, {}, {}'.format(file, exposure, gain, sens_temp)
# requirements:
# pip install soundfile numpy

import os
import sys
import struct

import numpy as np
import soundfile as sf

if (len(sys.argv)!=3):
  print("Usage "+sys.argv[0]+" FILE.TAP FILE.WAV")
  exit(1)

f = open(sys.argv[1], "rb")
t = f.read()

if (t[0:12]!=b"C64-TAPE-RAW") or (t[12]>1):
	print("Input file is not a TAP version 1 file")
	exit(1)

if ((len(t)-struct.unpack('<i',t[16:20])[0])!=20):
	print("File len mismatch!")
	print("Data len:",len(t)-20,"!=",struct.unpack('<i',t[16:20])[0])
	
t = t[20:]

o = sf.SoundFile(sys.argv[2],"w", samplerate=44100, channels=1, format='WAV', subtype='PCM_16', endian='FILE')

c=-1
offset=0

for i in range(len(t)):
	c=c+1
	if (c>=len(t)): break
	if (t[c]==0):
		cycles=offset+(struct.unpack('<i',t[c:c+4])[0]/256) * 44100 / 985248 
		offset=cycles-int(cycles)
		c=c+3
		data=np.full(int(cycles), 0.0, dtype=np.float32)
		o.write(data)
	else:
		cycles=offset+t[c] * 8 * 44100 / 985248
		offset=cycles-int(cycles)
		hw1=np.full(int(cycles/2), 0.75, dtype=np.float32)
		hw2=np.full(int(cycles/2), -0.75, dtype=np.float32)
		o.write(hw1)
		o.write(hw2)
				
f.close()
o.close()

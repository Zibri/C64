# requirements:
# pip install soundfile numpy

import os
import sys
import struct

import soundfile as sf

if (len(sys.argv)!=3):
  print("Usage "+sys.argv[0]+" FILE.WAV FILE.TAP")
  exit(1)

f = f=sf.SoundFile(sys.argv[1])
w = f.read()

o = open(sys.argv[2], "wb")
o.write(b"C64-TAPE-RAW\x01\x00\x00\x00\x00\x00\x00\x00")

counter=0
b=bytearray(1)
flen=0

for i in range(len(w)-1):
  counter=counter+1
  if(w[i]<0) and (w[i+1]>=0):
    taplen = int(((counter/f.samplerate) * 985248) / 8);
    if(taplen < 256):
      b[0]=taplen
      o.write(b)
      flen=flen+1
    else:
      cycles = int(((counter/f.samplerate) * 985248));
      o.write(b"\x00")
      o.write(struct.pack('<i', cycles)[:3])
      flen=flen+4
    counter=0

f.close()
o.seek(16)
o.write(struct.pack('<i', flen))
o.close()

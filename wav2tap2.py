# requirements:
# pip install soundfile numpy

import os
import sys
import struct

import soundfile as sf

if (len(sys.argv)!=3):
  print("Usage "+sys.argv[0]+" FILE.WAV FILE.TAP")
  exit(1)

f = sf.SoundFile(sys.argv[1])
w = f.read()

o = open(sys.argv[2], "wb")
data=bytearray()
counter=0
b=bytearray(1)


for i in range(len(w)-1):
  counter=counter+1
  if(w[i]<0) and (w[i+1]>=0):       # measure from rising edge
  #if (w[i]>=0) and (w[i+1]<0):    # measure from positive peak
    #taplen = int(counter/f.samplerate * 985248 / 8);
    taplen = int(counter/f.samplerate * 123156);
    if(taplen < 256):  # note: taplen rarely exceeds $70 (never seen it so far)
      data.extend(bytes([taplen]))
    else:
      cycles = counter/f.samplerate * 985248;
      cycles = int(cycles)
      data.extend(b"\x00"+struct.pack('<i', cycles)[:3])
    counter=0

f.close()

# remove initial rubbish:
#data=data[data.find(b"\x00")+4:]
#data=data[data.find(b"\x00")+4:]

data=b"C64-TAPE-RAW\x01\x00\x00\x00"+struct.pack('<i', len(data))+data

o.write(data)
o.close()

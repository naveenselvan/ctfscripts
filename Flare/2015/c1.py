cipher=[ 0x1F, 0x08, 0x13, 0x13, 0x04, 0x22, 0x0E, 0x11, 0x4D, 0x0D, 
  0x18, 0x3D, 0x1B, 0x11, 0x1C, 0x0F, 0x18, 0x50, 0x12, 0x13, 
  0x53, 0x1E, 0x12, 0x10]

for i in cipher:
    print(chr(i^125),end='')

import itertools
cipher=[95,193,50,12,127,228,98,6,215,46,200,106,251,121,186,119,109,73,35,14,20]

#j_runtimevalue=[0XBf,0xc6,0xc1,0x97,0xc9,0x24,0x12,0x34,0x82,0x35,0xb3,0x29,0xf9,0x64,0xf1,0x81,0x2c,0x1a,0x27,0x93,0xac]

array=[0x51,0xBF,0x07,0xFB,0xD6,0x32,0x5B,0xEE,0x22,0x4E,0xB3,0x7E,0x76,0xD0,0x6B,0x8D,0x90,0xAB,0x61,0x0D,0x6C,0x19,0x4F,0xCC,0xB4,0x69,0xCA,0x38,0x06,0x62,0x3E,0x0E,0x96,0x0F,0x08,0x28,0xB5,0x5E,0xD1,0x4D,0x15,0x3F,0x8C,0x2C,0x1E,0xF8,0xBA,0x44,0x5C,0x41,0x2A,0x45,0xBB,0x47,0x26,0x37,0x93,0x57,0xB0,0xB6,0x9A,0x84,0x75,0xD8,0x9F,0x9E,0xE0,0x91,0x50,0xCB,0x79,0xA6,0xBD,0xC2,0xD4,0x88,0xC5,0x1A,0x21,0x3D,0x00,0xAC,0x48,0x54,0xD2,0xFE,0x7C,0x68,0x8B,0xF4,0x4C,0x3A,0x99,0x3B,0x16,0x83,0xAA,0x6D,0xE1,0x09,0xA0,0xCF,0xD5,0xC0,0xDF,0x7A,0xD9,0xEF,0x87,0xA2,0x82,0x0A,0xAD,0x80,0xDA,0x34,0x46,0xB9,0xEA,0xE9,0x9B,0x39,0x74,0xE5,0xAF,0x2D,0xF3,0x73,0xB8,0x24,0x71,0xF9,0x14,0x52,0x27,0xF6,0x81,0xDE,0xE2,0x8A,0xC1,0x2F,0xA5,0x5D,0xFC,0xC7,0x92,0x8F,0x70,0xA7,0xA1,0x43,0x40,0xC4,0x7D,0x95,0x42,0xBC,0x23,0x59,0x63,0x6A,0x03,0xDD,0x1D,0x7F,0x49,0x66,0x3C,0xC9,0xEC,0xF2,0xF0,0x67,0xC8,0x20,0xD3,0xF1,0x77,0x10,0x1F,0x35,0xD7,0xC6,0x25,0x11,0xA8,0x13,0x04,0x0B,0x5F,0x01,0x1B,0x58,0xBE,0xFF,0x7B,0xF5,0xE7,0x65,0x86,0xFA,0x1C,0xB2,0xB7,0x02,0xED,0x98,0xE8,0x94,0x6E,0x29,0x9D,0x2E,0x0C,0x8E,0x89,0xFD,0xE6,0xE3,0x97,0x72,0xC3,0x4A,0xCE,0xDB,0xAE,0xCD,0xF7,0xEB,0x18,0x6F,0x64,0xB1,0x31,0xA3,0xA9,0x55,0xA4,0x2B,0x17,0x53,0x30,0x56,0x12,0xE4,0x9C,0x85,0x33,0x5A,0x4B,0x78,0x60,0x05,0xDC,0x36]
flag=''

i=0
j=0
for q in cipher:
      i = i + 1 & 255
      j= j + array[i] & 255
      b = array[i]
      array[i] = array[j]
      array[j] = b
      print(array[array[i] + array[j] & 0xFF])
      flag+=chr(q^(array[array[i] + array[j] & 0xFF]))       


print(flag)


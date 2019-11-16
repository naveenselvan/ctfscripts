def ROL(data, shift, size=32):
    shift %= size
    remains = data >> (size - shift)
    body = (data << shift) - (remains << size )
    return (body + remains)

def flag_check(str,bx):
    dx=bx
    dx=dx&3
    ah=1
    cf=1
    al=str^0xc7
    ah=ROL(ah,dx)
    al=al+ah+cf
    bx=bx+al
    return al,bx,ah



cipher=[ 0xAF, 0xAA, 0xAD, 0xEB, 0xAE, 0xAA, 0xEC, 0xA4, 0xBA, 0xAF,
  0xAE, 0xAA, 0x8A, 0xC0, 0xA7, 0xB0, 0xBC, 0x9A, 0xBA, 0xA5,
  0xA5, 0xBA, 0xAF, 0xB8, 0x9D, 0xB8, 0xF9, 0xAE, 0x9D, 0xAB,
  0xB4, 0xBC, 0xB6, 0xB3, 0x90, 0x9A, 0xA8]



char_set='-.@012345abcdefghijklmnopqrstuvwxyz_ABCDEFGHIJKLMNOPQRSTUVWXYZ{}'
bx=0

fl=''
for j in reversed(cipher):
    for i in char_set:
        ret=flag_check(ord(i),bx)
        if j == ret[0]:
            fl+=(i)
            bx=(ret[1])
            ah=(ret[2])
            break

print(fl)

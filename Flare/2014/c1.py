ba = bytearray(open('dat_secret', 'rb').read())

print ''.join(chr((b >> 4 | (b << 4 & 240)) ^ 41) for b in ba)

#https://github.com/Dvd848/CTFs/blob/master/2019_KipodAfterFree/dkdos.md
from z3 import *
import string, itertools

def hash(s):
    res = 0
    for c in s:
        res = res << 2
        res += c
        res = res & 0xFFFF
    return res

KEY_LEN = 8

key = [BitVec("{}".format(i), 16) for i in range(KEY_LEN)]
solver = Solver()
for i in range(KEY_LEN):
    solver.add(key[i] >= ord('!'))
    solver.add(key[i] <= ord('~'))

solver.add(hash(key) == 0xcfe1)
if solver.check() == sat:
    res = ""
    m = solver.model()
    print(m)
    for i in range(KEY_LEN):
        res += chr(

#NOte: I am not the Author
from z3 import *

s = [BitVec("s[%d]" %i,7 )for i in range(0,6)]
print(s)
z3_solver = Solver()
for i in range(0,len(s)):
	z3_solver.add(s[i] >= 0x40 , s[i] <= 0xff)

z3_solver.add( s[0] == s[5] )
z3_solver.add( s[0] + 1 == s[1] )
z3_solver.add( s[3] + 1 == s[0] )
z3_solver.add( s[2] + 4 == s[5] )
z3_solver.add( s[4] + 2 == s[2] )
z3_solver.add((s[3] ^ 0x72) == 0)

#0 1 2 3 4 5
#s t o r m s


if z3_solver.check() == sat:
	sol = z3_solver.model()

flag=""
for i in range(0,len(s)):
	flag +=chr(int(str(sol[s[i]])))
	
print(flag)


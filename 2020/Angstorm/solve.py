from z3 import *

x = Int('x')
y = Int('y')
solve(x+y==1142 ,x*y==302937)

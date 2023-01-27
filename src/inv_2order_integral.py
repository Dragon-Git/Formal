from z3 import (Solver,Int,Sum)

t = [Int("t_%d" % i) for i in range(64)]
d = [(t.index(i)+1)*i for i in t]

s = Solver()
for i in t:
    s.add(i>=0, i<=15)

s.add(Sum(*d)==23231)
c = s.check()
m = s.model()
print(s, c, m)

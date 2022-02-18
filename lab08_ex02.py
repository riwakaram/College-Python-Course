from sympy import sin, series, Symbol
from matplotlib import pylab
x = Symbol('x')
s10 = sin(x).series(x, 0, 10).removeO()
s20 = sin(x).series(x, 0, 20).removeO()
s = sin(x)
xx = []
y10 = []
y20 = []
y = []
for i in range(1000):
    xx.append(i / 100.0)
    y10.append(float(s10.subs({x: i / 100.0})))
    y20.append(float(s20.subs({x: i / 100.0})))
    y.append(float(s.subs({x: i / 100.0})))

pylab.plot(xx, y10, label='O(10)')
pylab.plot(xx, y20, label='O(20)')
pylab.plot(xx, y, label='sin(x)')
pylab.axis([0, 10, -4, 4])
pylab.xlabel('x')
pylab.ylabel('f(x)')
pylab.legend()
pylab.savefig('sympy.pdf')
pylab.savefig('sympy.png')
pylab.show()

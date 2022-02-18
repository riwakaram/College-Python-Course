"""example 1c"""
from matplotlib import pylab as p

x = p.arange(-3.14, 3.14, 0.01)
y = p.sin(x)
p.plot(x, y)
p.show()

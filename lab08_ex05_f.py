import numpy as N

t = N.arange(0, 2 * N.pi, 0.01)

from matplotlib import pylab

pylab.plot(t, N.sin(t), label='sin(t)')
pylab.plot(t, N.cos(t), label='cos(t)')
pylab.legend()
pylab.show()

import numpy as N
t = N.arange(0, 2 * N.pi, 0.01)

from matplotlib import pylab
pylab.subplot(2, 1, 1)
pylab.plot(t, N.sin(t))
pylab.xlabel('t')
pylab.ylabel('sin(t)')
pylab.subplot(2, 1, 2)
pylab.plot(t, N.cos(t))
pylab.xlabel('t')
pylab.ylabel('cos(t)')
pylab.show()

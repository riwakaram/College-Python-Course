import numpy as np
import scipy.interpolate
from matplotlib import pylab


def create_data(n):
    """Given an integer n, returns n data points x and values y as a numpy.array."""
    xmax = 5.
    x = np.linspace(0, xmax, n)
    y = - x ** 2
    # make x-data somewhat irregular
    y += 1.5 * np.random.normal(size=len(x))
    return x, y


# main program
n = 10
x, y = create_data(n)
# use finer and regular mesh for plot
xfine = np.linspace(0.1, 4.9, n * 100)
# interpolate with piecewise constant function (p=0)
y0 = scipy.interpolate.interp1d(x, y, kind='nearest')
# interpolate with piecewise linear func (p=1)
y1 = scipy.interpolate.interp1d(x, y, kind='linear')
# interpolate with piecewise constant func (p=2)
y2 = scipy.interpolate.interp1d(x, y, kind='quadratic')
pylab.plot(x, y, 'o', label='data point')
pylab.plot(xfine, y0(xfine), label='nearest')
pylab.plot(xfine, y1(xfine), label='linear')
pylab.plot(xfine, y2(xfine), label='cubic')
pylab.legend()
pylab.xlabel('x')
pylab.savefig('interpolate.pdf')
pylab.show()

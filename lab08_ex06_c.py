from scipy.integrate import odeint
import numpy as N


def f(y, t):
    """this is the rhs of the ODE to integrate, i.e. dy/dt=f(y,t)"""
    return -2 * y * t


y0 = 1  # initial value
a = 0  # integration limits for t
b = 2

t = N.arange(a, b, 0.01)
# values of t for which we require the solution y(t)
y = odeint(f, y0, t)  # actual computation of y(t)
from matplotlib import pylab  # plotting of results
pylab.plot(t, y)
pylab.xlabel('t')
pylab.ylabel('y(t)')
pylab.show()

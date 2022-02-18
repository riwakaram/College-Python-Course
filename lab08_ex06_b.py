from math import cos, exp, pi
from scipy.integrate import quad


# function we want to integrate
def f(x):
    return cos(2 * x * pi)


# call quad to integrate f from 0 to 1
res, err = quad(f, 0, 1)
print("The numerical result is {:f} (+-{:g})".format(res, err))

from sympy import integrate, Symbol, cos
x = Symbol('x')
i = integrate(cos(2 * x * pi), (x, 0, 1))
print("The analytical result is %f" % i)

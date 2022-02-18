from scipy.optimize import bisect
import math


def f(x):
    return 2 - x ** 2


x = bisect(f, 1, 2, xtol=1e-8)
print("The root x is approximately x=%14.12g,\nThe error is less than 1e-8." % x)
print("The exact error is %g." % (math.sqrt(2) - x))

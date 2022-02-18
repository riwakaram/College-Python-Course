from scipy.optimize import fsolve


def f(x):
    return x ** 3 - 2 * x ** 2


x = fsolve(f, 3)  # one root is at x=2.0
print("The root x is approximately x=%21.19g" % x)
print("The exact error is %g." % (2 - x))

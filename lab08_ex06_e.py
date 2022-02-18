from scipy.optimize import bisect


def f(x):
    """returns f(x)=x^3-2x^2. Has roots at x=0 (double root) and x=2"""
    return x ** 3 - 2 * x ** 2


# main program starts here
x = bisect(f, 1.5, 3, xtol=1e-6)
print("The root x is approximately x=%14.12g,\nThe error is less than 1e-6." % x)
print("The exact error is %g." % (2 - x))

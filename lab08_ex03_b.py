from sympy import Rational

dx_symbolic = Rational(1, 10)
dx = 0.1


def loop_sympy(n):
    x = 0
    for i in range(n):
        x = x + dx_symbolic
    return x


def loop_float(n):
    x = 0
    for i in range(n):
        x = x + dx
    return x


def time_this(f, n):
    import time
    starttime = time.time()
    result = f(n)
    stoptime = time.time()
    print("deviation is %16.15g" % (n * dx_symbolic - result))
    return stoptime - starttime


n = 100000
print("loop using float dx:")
time_float = time_this(loop_float, n)
print("float loop n=%d takes %6.5f seconds" % (n, time_float))
print("loop using sympy symbolic dx:")
time_sympy = time_this(loop_sympy, n)
print("sympy loop n=%d takes %6.5f seconds" % (n, time_sympy))
print("Symbolic loop is a factor %.1f slower." % (time_sympy / time_float))

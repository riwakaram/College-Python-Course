# # Sorting in Python
#
# # Ch. 12 -- Symbolic Computations
#
# # The following is the history of the Console
# # and the output of each statement
#
# from sympy import Symbol
# x = Symbol('x')
# type(x)
# <class 'sympy.core.symbol.Symbol'>
# y = Symbol('y')
# 2 * x - x/2
# 3*x/2
# del x
# del y
# del Symbol
# sorted([5, 3, 8, 1, 7])
# [1, 3, 5, 7, 8]
# [5, 3, 8, 1, 7].sort()
# a = [5, 3, 8, 1, 7]
# a.sort()
# a
# [1, 3, 5, 7, 8]
# sorted("This is a statement".split())
# ['This', 'a', 'is', 'statement']
# sorted("This is a statement".split(), key = str.lower)
# ['a', 'is', 'statement', 'This']
# a
# [1, 3, 5, 7, 8]
# a = [5, 3, 8, 1, 7]
# a.sort(reverse=True)
# a
# [8, 7, 5, 3, 1]
# from sympy import Symbol
# x = Symbol('x')
# type(x)
# <class 'sympy.core.symbol.Symbol'>
# y = Symbol('y')
# 2 * x - x / 2
# 3*x/2
# x + 2 * y - 3 * x / 2 + 2 * y
# -x/2 + 4*y
# import sympy
# x, y, z = sympy.symbols('x, y, z')
# x**2 - 2*y + x*z - 3*y
# x**2 + x*z - 5*y
# (x**2 - 2*y + x*z - 3*y).subs(y, 5)
# x**2 + x*z - 25
# (x**2 - 2*y + x*z - 3*y).subs(y, 5).subs(x, 3)
# 3*z - 16
# (x**2 - 2*y + x*z - 3*y).subs(y, 5).subs(x, 3).subs(z, -2)
# -22
# a = sympy.Rational(1, 2)
# a
# 1/2
# type(a)
# <class 'sympy.core.numbers.Half'>
# b = sympy.Rational(1, 15)
# type(b)
# <class 'sympy.core.numbers.Rational'>
# a * b
# 1/30
# b = sympy.Rational(43, 30)
# b
# 43/30
# b = sympy.Rational(46, 30)
# b
# 23/15
# a * b
# 23/30
# a
# 1/2
# a / b
# 15/46
# a + b
# 61/30
# a - b
# -31/30
# float(a)
# 0.5
# a = sympy.Rational(2, 3)
# a
# 2/3
# float(a)
# 0.6666666666666666
# a.evalf()
# 0.666666666666667
# a.evalf(4)
# 0.6667
# a.evalf(100)
# 0.6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666667
# from sympy import Symbol, sin, cos, sqrt, diff, exp
# diff(sin(x), x)
# cos(x)
# diff(sin(x), y)
# 0
# diff(-2 + x -3 * x**2 +5*x**4)
# 20*x**3 - 6*x + 1
# diff(exp(-x**2 / 3), x)
# -2*x*exp(-x**2/3)/3
# diff(-2 + x -3 * x**2 +5*x**4, x, x)
# 6*(10*x**2 - 1)
# diff(-2 + x -3 * x**2 +5*x**4, x, x, x)
# 120*x
# diff(diff(-2 + x -3 * x**2 +5*x**4, x))
# 60*x**2 - 6
# from sympy import integrate
# integrate(x**2, x)
# x**3/3
# integrate(x**2, (x, 0, 1))
# 1/3
# y = sympy.Function("y")
# x = Symbol('x')
# y_ = sympy.Derivative(y(x), x)
# print(sympy.dsolve(y_ + 5*y(x), y(x)))
# Eq(y(x), C1*exp(-5*x))
# sin(x).series(x)
# x - x**3/6 + x**5/120 + O(x**6)
# sin(x).series(x, 10)
# sin(10) + (x - 10)*cos(10) - (x - 10)**2*sin(10)/2 - (x - 10)**3*cos(10)/6 + (x - 10)**4*sin(10)/24 + (x - 10)**5*cos(10)/120 + O((x - 10)**6, (x, 10))
# sin(x).series(x, 0, 10)
# x - x**3/6 + x**5/120 - x**7/5040 + x**9/362880 + O(x**10)
# sin(x).series(x, 0, 20)
# x - x**3/6 + x**5/120 - x**7/5040 + x**9/362880 - x**11/39916800 + x**13/6227020800 - x**15/1307674368000 + x**17/355687428096000 - x**19/121645100408832000 + O(x**20)
# sin(x).series(x, 0, 20).removeO()
# -x**19/121645100408832000 + x**17/355687428096000 - x**15/1307674368000 + x**13/6227020800 - x**11/39916800 + x**9/362880 - x**7/5040 + x**5/120 - x**3/6 + x
# sin(x).series(x, 0, 10).removeO()
# x**9/362880 - x**7/5040 + x**5/120 - x**3/6 + x

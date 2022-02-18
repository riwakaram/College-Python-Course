# Series expansion and plotting

# from sympy import sin, series, Symbol
# from matplotlib import pylab
# x = Symbol('x')
# s10 = sin(x).series(x, 0, 10).removeO()
# s20 = sin(x).series(x, 0, 20).removeO()
# s = sin(x)
# xx = []
# y10 = []
# y20 = []
# y = []
# for i in range(1000):
#     xx.append(i / 100.0)
#     y10.append(float(s10.subs({x: i / 100.0})))
#     y20.append(float(s20.subs({x: i / 100.0})))
#     y.append(float(s.subs({x: i / 100.0})))
#
# pylab.plot(xx, y10, label='O(10)')
# pylab.plot(xx, y20, label='O(20)')
# pylab.plot(xx, y, label='sin(x)')
# pylab.axis([0, 10, -4, 4])
# pylab.xlabel('x')
# pylab.ylabel('f(x)')
# pylab.legend()
# pylab.savefig('sympy.pdf')
# pylab.savefig('sympy.png')
# pylab.show()


# Linear equations and matrix inversion
# 5 x1 + 4 x2 = z
# 3 x1 - 6 x2 = 2 z
# A = [5,  4]
#     [3, -6]
# b = [ 1 ]
#     [ 2 ]
# x = [ x1 ]
#     [ x2 ]
# Solve : Ax = b => x = inverse(A) b

# from sympy import Matrix, symbols, solve_linear_system
#
# x, y, z = symbols('x, y, z')
# system = Matrix(([5, 4, 1 * z], [3, -6, 2 * z]))
# print(system)
# sol = solve_linear_system(system, x, y)
# print(sol)
# for k in sol.keys():
#     print(k, '=', sol[k].subs({z: 1.0}).evalf(4))

# from sympy import symbols, solve, Eq
#
# x, y, z = symbols('x, y, z')
# print(solve((Eq(5 * x + 4 * y, 1 * z), Eq(3 * x - 6 * y, 2 * z)), x, y))
# print(solve((5 * x + 4 * y - 1 * z, 3 * x - 6 * y - 2 * z), x, y))


# Non linear equations

# Chapter 14 - NumPy
# NumPy

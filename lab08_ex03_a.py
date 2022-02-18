from sympy import Rational

dx = Rational(1, 10)
x = 0
while x != 1.0:
    x = x + dx
    print("Current x=%4s = %3.1f" % (x, x.evalf()))
print("Reached x=%s" % x)

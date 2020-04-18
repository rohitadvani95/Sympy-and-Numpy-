import sympy as sym
from sympy import Symbol
from sympy import sin, cos, tan
from sympy import diff
from sympy import limit
from sympy.abc import delta
from sympy import summation, oo, symbols, log, integrate, erf, exp, pi, sinh
from sympy import Function, dsolve, Integral
from sympy import Matrix, pprint

i, n, m = symbols('i n m', integer = True)
#from sympy import 

x = Symbol('x')
y = Symbol('y')
z = Symbol('z')

sym.diff(x**5)

sym.diff((6*x**3) + (5*x**2)+(4))

print(sym.diff(x**5))

print(sym.diff((6*x**3) + (5*x**2)+(4)))

f1 = diff(sin(x), x)

print(f1)

f2 = diff(sin(2*x), x)

print(f2)

SeriesExp1 = cos(x).series(x,0,15)
print(SeriesExp1)


print(summation(2*i - 1, (i, 1, n)))

print(summation(i,(i, 0, 2)))

integral1 = integrate(7*x**5)
print(integral1)

integral2 = integrate(log(x))
print(integral2)

f = Function('f')

f(x).diff(x,x)+f(x)

print(dsolve(f(x).diff(x,x) + f(x), f(x)))

pprint(Matrix([[1,0],[0,1],[0,0]]))

d1 = sym.diff((x**2 - 3*x + 5)**3)

print(d1)

f = x**2 * y * z**5

print(sym.diff(f,x))
print(sym.diff(f,y))
print(sym.diff(f,z))

pprint(Integral(x**5, x), use_unicode=True)



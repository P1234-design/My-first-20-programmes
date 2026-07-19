import cmath
a=float(input('a:'))
b=float(input('b:'))
c=float(input('c:'))

d=(b**2)-(4*a*c)
print('discriminent:-',d)
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)
print('The soluton are{0} and {1}'.format(sol1,sol2))
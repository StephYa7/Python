# Найти корни квадратного уравнения Ax² + Bx + C = 0

# D = b ** 2 - 4ac
# x = -b/2a

a = int(input())
b = int(input())
c = int(input())

D = b**2 - 4 * a * c

print(D)

if D < 0:
    print('Корней нет')
elif D== 0:
    x=-b/2*a

    print(x)
else:
    x1=(-b+D**0.5)/2*a
    x2=(-b-D**0.5)/2*a

    print(round(x1,2),round(x2,2))
# def sum(x, y):
#     return x+y


# def mylt(x, y):
#     return x*y

# f = lambda q, w : q+w

# def f(x):
#     return x**3

# list = [(i, f(i)) for i in range(1, 21) if i % 2 == 0]

# print(list)


# def select(f, col):
#     return [f(x) for x in col]

# def where(f, col):
#     return[x for x in col if f(x)]

# data = '1 2 3 5 8 15 23 38'.split()
# res = select(int, data)
# res = where(lambda x : not x % 2, res)
# res = select(lambda x : (x,x**2),res)
# print(res)


# list = [(i, i**2) for i in data if i % 2 == 0]
# print(list)


# data = [x for x in range(10)]
# res = list(filter(lambda x: not x % 2, data))
# print(res)



user = ['u1', 'u2', 'u3']
ids = [4, 5, 9, 14, 7]
data = list(zip(user,ids))
print (data)




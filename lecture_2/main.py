# list_1 = []
# list_1 = list()
# list_1 = [1, 2, 3, 8]

# # for i in list_1:
# #     print(i)

# # print(len(list_1))

# print(list_1[0])

# list_1 = [1, 5]
# print(list_1)
# list_1.append(8)
# print(list_1)
# list_1.append(85)
# print(list_1)

# list_1 = []
# print(list_1)
# for i in range(5):
#     list_1.append(i)
#     print(list_1)

# list_1 = [12, 7, -1, 21, 0]
# print(list_1.pop(0))

# list_1 = [12, 7, -1, 21, 0]
# print(list_1.insert(2, 11))
# print(list_1)

# Кортежи

# t = ()

# print(type(t))

# t = (1, 2, 3,)
# print(type(t))

# Список в кортеж

# v = [1, 8, 9]
# print(v)
# print(type(v))

# v = tuple(v)
# print(v)
# print(type(v))

# a = 1
# b = 2
# a, b = 1, 2
# a = b = 1


# a,b,c = v
# print(a, b, c)

# t = (1, 2, 3, 5,)

# for i in t:
#     print(i)

# for i in range(len(t)):
#     print(t[i])

# t[0] = 2 

# Словари

# d = {}
# d = dict()

# d['q'] = 'qwerty'
# print(d)

# d['w'] = 'werty'
# print(d['q'])

# dictionary = {}
# dictionary = {'up': 'вверх'}

# # del dictionary ['up'] #удаление элемента
# print(dictionary.items())

# for (k, v) in dictionary.items():
#     print(k, v)

# Множества

# colors = {'red', 'green', 'blue'}
# print(colors)
# colors.add('red')
# print(colors)
# colors.add('grey')
# print(colors)
# colors.remove('red')
# print(colors)
# colors.discard('red')
# print(colors)
# colors.clear()
# print(colors)

# q = set()

# Операции со множествами в Python

# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy()
# print(c)
# u = a.union(b)
# print(u)
# i = a.intersection(b)
# print(i)
# d1 = a.difference(b)
# print(d1)
# dr = b.difference(a)
# print(dr)
# q = a.union(b).difference(a.intersection(b))
# print(q)

# Замороженное множество

a = {1, 8, 6}

b = frozenset(a)

print(b)
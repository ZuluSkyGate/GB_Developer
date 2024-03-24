# def hello(name):
#     return f"Hello, {name}"

# def bye(name):
#     return f"{name}, bye-bye"

# def create_phrase(func):
#     name = input("Введите свое имя ")
#     return func(name)

# def create_dialog(funcs):
#     name = input("Введите свое имя ")
#     res = ""
#     for func in funcs:
#         res += f"{func(name)}\n"
#     return res


# # funcs = [hello, bye]
# # print(create_dialog(funcs))
# # print(create_phrase(hello))
# # print(create_phrase(bye))

# def calc_power(degree):
#     def power(base):
#         return base ** degree
#     return power

# # print(calc_power(3) (2))
# square = calc_power(2)
# cube = calc_power(3)
# # print(square(9) )
# # print(cube(4))


# # l1 = [1,2,lambda x: x ** 2 if x % 2 else 0,3,4]
# # print(l1[2] (7))

# # функция будет возводить в квадрат нечетные и обнулять четные
# # square_even = lambda x: x ** 2 if x % 2 else 0
# # print(square_even(9))
# # print(square_even(8))

# # calc = {
# #     "+": lambda x,y: x + y,
# #     "-": lambda x,y: x - y,
# #     "*": lambda x,y: x * y,
# #     "/": lambda x,y: x / y,
# # }
# # s = input("Введите арифметическое выражение через пробел ")
# # first, op, second = s.split()
# # print(f"Результат равен {calc[op] (int(first), int(second))}")

# # print(sp := list(range(11)))

# # print( list(map (lambda x: x ** 2, sp)) )
# # print( *map (lambda x: x ** 2, sp) )
# # print( *map (lambda x: x ** 2 if x % 2 else 0, sp) )

# # print( *filter (lambda x: x % 2, sp) )

# # x = 10
# # if x % 2:
# #     res = "Нечетный"
# # else:
# #     res = "Четный"
# # print(res)

# # print("Нечетный" if x%2 else "Четный")


# # l1 = [1,2,3]  #маленький пакет с продуктами
# # print([l1, 4,5])   # маленький пакет внутри большого
# # print([*l1, 4,5])   # вытащили продукты из маленького пакета, теперь все на одном уровне   


# Задача №47. Общее обсуждение У вас есть код, который вы не можете менять(так часто бывает, когда код в глубине программы используется множество раз
# и вы не хотите ничего сломать): transformation = <???> values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] 
# или любой другой список transormed_values = list(map(transformation, values)) Единственный способ вашего взаимодействия с этим кодом - посредством
# задания функции transformation. Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать список значений, а нужно получить его как есть.
# Напишите такое лямбда-выражение transformation, чтобы transformed_values получился копией values.

# lambda x: x  ?

# Задача №49. Решение в группах Планеты вращаются вокруг звезд по эллиптическим орбитам. Назовем самой далекой планетой ту, 
# орбита которой имеет самую большую площадь. Напишите функцию f ind_farthest_orbit(list_of_orbits), которая среди списка орбит
# планет найдет ту, по которой вращается самая далекая планета. Круговые орбиты не учитывайте: вы знаете, что у вашей звезды таких планет нет,
# зато искусственные спутники были были запущены на круговые орбиты. Результатом функции должен быть кортеж, содержащий длины полуосей эллипса орбиты самой далекой планеты. 
# Каждая орбита представляет из себя кортеж из пары чисел - полуосей ее эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b, где a и b - длины полуосей эллипса. 
# При решении задачи используйте списочные выражения. Подсказка: проще всего будет найти эллипс в два шага: сначала вычислить самую большую площадь эллипса, а затем найти
# и сам эллипс, имеющий такую  площадь. Гарантируется, что самая далекая планета ровно одна

# Ввод: orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)] print(*find_farthest_orbit(orbits)) Вывод: 2.5 10 и самая далекая планета это № 2

     

# S = pi * a * b
# print(* find_farthest_orbit(orbits))

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)] 

# def find_farthest_orbit(orbits):
#     findArea_orbits = list(map(lambda x: x[0] * x[1] if x[0] != x[1] else -1, orbits))
#     maxArea_index = findArea_orbits.index(max(findArea_orbits))
#     return orbits[maxArea_index],maxArea_index + 1


# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))

def find_farthest_orbit(list_of_orbits):
        squares = list(map(lambda a: a[0]*a[1] if a[0] != a[1] else 0, list_of_orbits))
        return *list_of_orbits[squares.index(max(squares))], f"планета № {squares.index(max(squares))+1}"

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)] 
print(*find_farthest_orbit(orbits))


# Задача №51. Решение в группах Напишите функцию same_by(characteristic, objects), которая проверяет, все ли объекты имеют одинаковое значение некоторой характеристики, 
# и возвращают True, если это так. Если значение характеристики для разных объектов отличается - то False. Для пустого набора объектов, функция должна возвращать True. 
# Аргумент characteristic - это функция, которая принимает объект и вычисляет его характеристику. 

# Ввод: values = [0, 2, 10, 6] if same_by(lambda x: x % 2, values): print(‘same’) else: print(‘different’) Вывод: same

# def same_by(characteristic, objects):
#     result_list=[]
#     result_list = list(map(characteristic,objects))
#     flag = True
#     for i in range(len(result_list)-1):
#         if result_list[i]!=result_list[i+1]:
#             flag=False
#     return flag

# values = [1, 2, 10, 6] 
# if same_by(lambda x: x % 2, values):
#     print('same') 
# else:
#      print('different')

def same_by(characteristic, objects): 
    # result = list(filter(characteristic, objects))
    # return len(result) == len(objects) or not len(result)
    size = len(set(map(characteristic, objects)))
    return size < 2

values = [] 
if same_by(lambda x: x % 2, values): 
    print("same") 
else: 
    print("different")
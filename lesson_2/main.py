# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является,
# то есть выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи,
# выведите число -1. Input:     5 Output:  6


# n = 6
# i = 1
# a = 1
# while i < n + 1:
#     a* = i
#     i+ = i
# print(f"!N({n}) = {a}")
    
    
# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while
# Input: 5
# Output: 120

# a = 5
# i = 2
# fib1, fib2 = 1, 1    
# while fib2 < a:
#     fib1, fib2  = fib2, fib1 + fib2
#     i += 1
# if fib2==a:
#     print(f"{i}")
# else:
#     print(f"-1")


# задача 2, числа фибоначчи

# number = int (input("Введите исходное число: "))
# first_number = 0
# second_number = 1
# current = 0
# i = 2 
# print (f"{first_number} счетчик 1")
# print (f"{second_number} счетчик 2")

# while second_number < number:
#     current = second_number + first_number
#     first_number = second_number
#     second_number = current
#     i += 1
#     print (f"{second_number} счетчик {i}")

# if number == 0:
#     print(1)
# elif number < second_number:
#     if number- first_number < second_number - number:
#         print(f"ближайшее число {first_number}, его нумер {i-1}")
#     elif number- first_number == second_number - number:
#         print(f"ближайшее числа {first_number} и {second_number}, за нумерами {i-1} и {i}")
#     else:
#         print(f"ближайшее число {second_number}, его нумер {i}")
    
# else:
#     print(i) 

#[0,1,1,2,3,5]

#Задача 1
# n = int (input("Введите число: "))
# i = 1
# f = 1
# while i <= n:
#     f *= i
#     i += 1
# print (F'факториал числа {n} равен {f}')


# Задача №15. Решение в группах 15. Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. Но вот незадача: арбузов слишком много и он не знает 
# как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему! Пользователь вводит одно число N – количество арбузов. Вторая строка 
# содержит N чисел, записанных на новой строчке каждое. Здесь каждое число – это масса соответствующего арбуза Input: 5 -> 5 1 6 5 9 Output: 1 9 11


# n = int(input("Введите количество арбузов: "))
# melones = []
# for e in range(n):
#     melones.append(int(input("Введите вес арбуза: ")))

# min = melones[0]
# max = melones[0]
# count = 0
# while count < len(melones):
#     if melones[count] < min:
#         min = melones[count]
#         count += 1
#     else:
#         count += 1

# count = 0
# while count < len(melones):
#     if melones[count] > max:
#         max = melones[count]
#         count += 1
#     else:
#         count += 1


# print(f"Арбуз для тёщи {min}")
# print(f"Арбуз для Ивана {max}")


# Задача №13. Решение в группах Уставшие от необычно теплой зимы, жители решили узнать, действительно ли это самая длинная оттепель за всю историю наблюдений
# за погодой. Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями статистики за прошлые годы. Их интересует, сколько дней длилась самая
# длинная оттепель. Оттепелью они называют период, в который среднесуточная температура ежедневно превышала 0 градусов Цельсия. Напишите программу, помогающую 
# синоптикам в работе. Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках располагается N целых чисел. 
# Каждое число – среднесуточная температура в соответствующий день. Температуры – целые числа и лежат в диапазоне от –50 до 50 
# Input:    6 -> -20 30 -40 50 10 -10 Output: 2

# Общее количество рассматриваемых дней (1 ≤ N ≤ 100)

# import random

# flag = True
# while flag:
#     N = int(input("Введите количество рассматриваемых дней (1 ≤ N ≤ 100): "))
#     if 1 <= N <= 100:
#         flag = False
# temp_list = []
# for i in range(N):
#     t = random.randint(-50, 51)
#     temp_list.append(t)
# print('Среднесуточные температуры: ')
# print(temp_list)
# max_warm_days = 0
# warm_days = 0
# for temp in temp_list:
#     if temp > 0:
#         warm_days+=1
#     else:
#         if warm_days > max_warm_days:
#             max_warm_days = warm_days
#         warm_days =0

# print(max_warm_days)


# temp_list = [ -20, 30, -40, 50, 10, 10]
# # temp_list = []
# # for i in range(N):
# #     t = random.randint(-50, 51)
# #     temp_list.append(t)
# print('Среднесуточные температуры: ')
# print(temp_list)
# max_warm_days = 0
# warm_days = 0
# for temp in temp_list:
#     if temp > 0:
#         warm_days+=1
#         if warm_days > max_warm_days:
#             max_warm_days = warm_days
#     else:
#         warm_days =0
# print(max_warm_days)
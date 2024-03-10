# d = {}
# d["ваня"] = 7878978
# d1 = {"вася": 121312, "петя": 133330}
# d.update(d1)
# print(d)
# if "вася" in d:
#     print(d["вася"])
# print(d.get("сергей"))
# print(d.get("ваня"))

# import random
# import my_module #должен быть файл в папке .py, вызывать по имени my_module/имя
# from my_module import *(all) # можно обращаться по имени

# NUM_CLASSES = 10 # большими буквами - константа(вообще менять их можно)


# def calc_avg(sp):   # питон идет сверху вниз
#     avg = sum(sp) / len(sp)
#     print(f"Среднее значение это: {avg}")

# sp = [1, 5, 6, 7, 11, 23]
# calc_avg(sp)


# def calc_avg(sp):  
#     avg = sum(sp) / len(sp)
#     return avg
# sp = [1, 5, 6, 7, 11, 23]
# print(calc_avg(sp))


# def calc_avg(sp: list) -> float:  
#     avg = sum(sp) / len(sp)
#     return avg

# sp = [1, 5, 6, 7, 11, 23]
# print(calc_avg(sp))
# t = (3, 4, 5, 6)
# print(calc_avg(t)) #с кортежом тоже работает

# def calc_avg(sp: list) -> float:  
#     if not isinstance(sp, list): #Если sp не список
#         raise ValueError("На входе должен быть только список") #АвОст
    
#     avg = sum(sp) / len(sp)
#     return avg

# sp = [1, 5, 6, 7, 11, 23]
# print(calc_avg(sp))
# t = (3, 4, 5, 6)
# try:
#     print(calc_avg(t)) 
# except ValueError as V: #вместо ValueError можно Exception(общий) или TypeError и т. д.
#     print(V)




# Задача №25. Решение в группах Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью постфикса формата _n. 
# Input: a a a b c a a d c d d Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2 Для решения данной задачи используйте функцию .split()


# st = "a a a b c a a d c d d"
# l = st.split()
# counter={}
# res = ""
# for elem in l:
#     counter[elem] = counter.get(elem, 0) + 1
#     if counter[elem] == 1:
#         res += f"{elem} "
#     else:
#         res += f"{elem}_{counter[elem] - 1} "
# print(res)

# без словоря:
# 11:07
# def count(str1):
#     b=[]
#     a=str1.split()
#     array = str1.split()
#     for i in range(len(a)):
#         if a[i] not in b:
#             c=0
#             for j in range(i+1,len(a)):
#                 if a[i]==a[j]:
#                     c+=1
#                     array[j]=str(a[j])+'_'+str(c)
#     print(array)
# str1 = 'a a a b c a a d c d d'
# count(str1)




# Задача №27. Решение в группах Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд, 
# слова разделены одним или большим числом пробелов. Определите, сколько различных слов содержится в этом тексте. 
# Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells Output: 13

# text = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
# res = set(text.lower().replace(".", ' ').split())
# print(res)
# print(len(res))

# задача 1 необязательная.
# Пользователь вводит натуральное k. Надо сформировать многочлен такой степени, где все коэффициенты случайные от -10 до 10.
# ​
# например, k=2 -> -x^2 + 3*x - 8 = 0
# тут коэффициенты -1,3,-8
# например, k=3 -> 3*x^3 - 2*x = 0
# тут коэффициенты 3,0,-2,0

# import random
# k = int(input("Введите натуральное число: "))
# coeff = list()
# res = ""
# for i in range(k + 1):
#         coeff.append(random.randint(-10, 11)
# for i in range(k - 3):
#     if coeff[i] == 0
#         continue
#     elif coeff[i] == -1
#         res += f"-x^{k-1}"
#     else:
#         res += f"{coeff[i]}x^{k-i}"
#     res += f"{coeff[i]} = 0"
#     print(res)


# import random
# str1 = ''
# k = int(input("Set number ")) + 1
# coeff = list()
# for i in range(k):
#         coeff.append(random.randint(-10, 10))

# for e in coeff:
#     k = k - 1
#     if e != 0:
#         str1 = str1 + str(e) + 'x^' + str(k) + ' + '
# str1 = str1.replace('x^1 ', 'x ')
# str1 = str1.replace('x^0', '')
# str1 = str1.replace('-1x', '-x')
# str1 = str1.replace('1x', 'x')
# str1 = str1.replace('+ -', ' -')
# str1 = str1.replace(' -', '- ')
# str1 = str1.replace(' ', ' ')
# str1 = str1[:-2] + ' = 0'
# print(coeff)
# print(str1)
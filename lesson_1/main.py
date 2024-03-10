# Решение 1.1
#n = 700
#m = 750
#print(m//n + 1%(m%n + 1))

# Решение 1.2
# def days_to_complete_route(n, m):
#     return (m + n - 1) // n

# Решение 1.3
# n = 700
# m = 750
# days = days_to_complete_route(n, m)
# print("Output:", days)

# Решение 2.1
# cl1 = int(input("Введите количество учащихся в первом классе: "))
# cl2 = int(input("Введите количество учащихся во втором классе: "))
# cl3 = int(input("Введите количество учащихся в третьем классе: "))
# total = (cl1 + 1) // 2 + (cl2 + 1) // 2 + (cl3 + 1) // 2
# print("Минимальное количество парт, которое нужно приобрести:", total)

# Решение 3.1
# i = int(input("Введите номер вагона Вити: "))
# j = int(input("Введите номер вагона: "))
# if i == j:
#     print("Определить невозможно")
# else:
#     j+=i-1
#     print(j)

# Решение 3.2
# year = int(input("Введите год: "))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#      print("YES")
# else:
#    print("NO")

# Решение доп. задания 3.3
# num = float(input("Введите любое целое число: "))
# num = abs(num)
# sum = 0
# while (num != 0):
#     sum = sum + num % 10
#     num = num // 10
# print("Сумма цифр числа равна: ", sum)

number = float(input("Введите дробное число: "))

number = abs(number) 
number = int(number) 

total_sum = 0 

while number > 0: 
    digit = number % 10
    total_sum += digit 
    number //= 10 

print("Сумма цифр числа:", total_sum) 







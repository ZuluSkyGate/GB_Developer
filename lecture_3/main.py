# def sum_numbers(n, y = 'Hello'):
#     summa = 0
#     for i in range(1, n+1):
#         summa += i
#     return summa
    
# a = sum_numbers(5, 'qwerty')

# print(a)

def sum_str(*args):
    res = ''
    for i in args:
        for i in args:
            res += i
        return res
print(sum_str('q', 'e', 'l'))
print(sum_str('q', 'e', 'l', 'r', 'f'))
print(sum_str(1, 8, 9))

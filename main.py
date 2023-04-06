# n = int(input())
# if n % 2 == 0:
#     print('True')
# else:
#     print('False')
# if n > 0:
#     print('True')
# else:
#     print('False')
# if -5 <= n <= 5:
#     print('True')
# else:
#     print('False')
# if n % 3 == 0 and n % 4 == 0 and n % 7 != 0:
#     print('True')
# else:
#     print('False')
# if 99 < n < 1000 or -1000 < n < -99:
#     print('True')
# else:
#     print('False')
#
# n1, n2, n3, n4 = [int(i) for i in input().split('.')]
# if 0 <= n1 <= 255 and 0 <= n2 <= 255 and 0 <= n3 <= 255 and 0 <= n4 <= 255:
#     if n1 + n2 + n3 + n4 != 0 and n1 + n2 + n3 + n4 != 1020:
#         print('True')
#     else:
#         print('False')
# else:
#     print('False')
#
# if (n := int(input())) % 7 == 0:
#     print('пн')
# elif n % 7 == 1:
#     print('вт')
# elif n % 7 == 2:
#     print('ср')
# elif n % 7 == 3:
#     print('чт')
# elif n % 7 == 4:
#     print('пт')
# elif n % 7 == 5:
#     print('сб')
# elif n % 7 == 6:
#     print('вс')
#
# a = int(input())
# b = int(input())
# c = int(input())
# d = [a, b, c]
# print(min(d))
#
# a = input()
# b = input()
# if len(a) > 4 and len(b) > 8 and a != b:
#     print('True')
# else:
#     print('False')
#
# command = input()
# match command:
#     case "Привет":
#         print('Привет!')
#     case "Как дела?":
#         print("Все классно!")
#     case 'Пока':
#         print("До скорой встречи!")
#     case _:
#         print('Прости, я еще не знаю таких фраз :(')
#
# s = input()
# match s:
#     case "Flask":
#         print('Python(Flask),Backend-dev')
#     case "Django":
#         print('Python(Django),Backend-dev')
#     case "Fast-API":
#         print('Python(Fast-API),Backend-dev')
#     case "Angular":
#         print('JavaScript/TypeScript(Angular),Frontend-dev')
#     case "React":
#         print('JavaScript/TypeScript(React),Frontend-dev')
#     case "Vue":
#         print('JavaScript/TypeScript(Vue),Frontend-dev')
#     case "Flutter":
#         print('JavaScript(Flutter),Cross-Mobile-dev')
#     case "React Native":
#         print('JavaScript(React Native),Cross-Mobile-dev')
#     case "Pandas":
#         print('Python(Pandas),Data-Scientist')
#     case "skit-learn":
#         print('Python(skit-learn),Data-Scientist')
#     case "keras":
#         print('Python(keras),Data-Scientist')
#     case _:
#         print('модель еще не обучена')
# # от авторов курса
# match s := input():
#     case "Flask" | "Django" | "Fast-API" as f:
#         print("Python" + "(" + f + ")," + "Backend-dev")
#     case "Angular" | "React" | "Vue" as f:
#         print("JavaScript/TypeScript" + "(" + f + ")," + "Frontend-dev")
#     case "Flutter" | "React Native" as f:
#         print("JavaScript" + "(" + f + ")," + "Cross-Mobile-dev")
#     case "Pandas" | "skit-learn" | "keras" as f:
#         print("Python" + "(" + f + ")," + "Data-Scientist")
#     case _:
#         print("модель еще не обучена")
#
# a = [int(i) for i in input().split()]
# for el in a:
#     print(el)
#
# n = int(input())
# res = 1
# if n == 0:
#     print('1')
# else:
#     for i in range(1, n + 1, 1):
#         res *= i
#     print(res)
#
# import sys
#
# print(sys.getsizeof(0))
#
#
# def has_upper_case(string):
#     for sym in string:
#         if sym.isupper():
#             return True
#     return False
#
#
# f = open('dataset_24465_4.txt', 'r')
# x = f.read().splitlines()
# print(x)
# y = x
# y.reverse()
# print(y)
# b = open('test.txt', 'w')
# contents = '\n'.join(y)
# b.write(contents)
# f.close()
# b.close()
#
# import os
# import os.path
#
# print(os.getcwd())
# print(os.listdir())
# for current_dir, dirs, files in os.walk('.'):
#     print(current_dir)
#     print('\n')
#     print(dirs)
#     print('\n')
#     print(files)
#     print('\n')
#
# year = int(input())
#
#
# def is_leap_year(year):
#     if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
#         print('True')
#     else:
#         print('False')
#
#
# is_leap_year(year)
#
#
# def is_leap_year(year):
#     return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
#
#
# def string_or_not(s):
#     if isinstance(s, str):
#         return 'yes'
#     else:
#         return 'no'
#
#
# print(string_or_not(5))
#
#
# def normalize_url(url):
#     if url[:7] == 'http://':
#         return 'https://' + url[7:]
#     elif url[:8] == 'https://':
#         return url
#     else:
#         return 'https://' + url
#
#
# print(normalize_url('https://ya.ru'))
#
#
# def print_numbers(n):
#     i = n
#     while 0 < i:
#         print(i)
#         i -= 1
#     print('finished!')
#
#
# print(print_numbers(6))
# import numbers
#
# x = int(input())
#
# i = x
#
#
# def closest_mod_5():
#     y = (x + 4) // 5
#     return y * 5
#
#
# print(closest_mod_5())
#
# n, k = map(int, input().split())
#
#
# def C(n, k):
#     if k == 0:
#         return 1
#     elif k > n:
#         return 0
#     else:
#         return C(n=n - 1, k=k) + C(n=n - 1, k=k - 1)
#
#
# print(C(n, k))
#
# n = int(input())
#
# if 5 <= n < 10 or 101 < n <= 200:
#     print('True')
# else:
#     print('False')
#
# n = int(input())
#
# if n % 2 == 0:
#     print(n + 10)
# else:
#     print(n - 10)
#
#
# def convert_to(number, base, upper=False):
#     if number == 0:
#         return 0
#     else:
#         digits = '0123456789abcdefghijklmnopqrstuvwxyz'
#         if base > len(digits): return None
#         result = ''
#         while number > 0:
#             result = digits[number % base] + result
#             number //= base
#         return result.upper() if upper else result
#
#
# n = int(input())
# print(convert_to(n, 5))
# nums = [int(i) for i in input().split()]
# lst = []
# for i in range(len(nums) - 1):
#     lst.append(nums[i] + nums[i + 1])
# for elem in lst:
#     print(elem, end=' ')
#
# nums = [int(i) for i in input().split()]
# a = set(nums)
# b = max(a)
# a.remove(b)
# c = max(a)
# print(c)
#
# nums = [int(i) for i in input().split()]
# a = [0]
# i = 0
# for num in nums:
#     if num == 0:
#         nums.remove(0)
#         i += 1
# for num in nums:
#     if num == 0:
#         nums.remove(0)
#         i += 1
# b = a * i
# lst = nums + b
# for elem in lst:
#     print(elem, end=' ')
#
# nums = [int(i) for i in input().split()]
# print(nums)
#
# for i in range(len(nums) - 1):
#     if nums[i] % 2 != 0:
#         nums.remove(i)
#         print(nums)
#
# print(nums)
#
# values = input().split()
#
# for i in range(len(values)):
#     print(values[i] + '!')
#
# a = {int(i) for i in input().split()}
# d = 0
# for i in a:
#     z = i ** 2
#     d = d + z
# print(d)
# b = set()
# while True:
#     try:
#         c = int(input())
#         b.add(c)
#         if c == 0:
#             break
#     except:
#         break
#
# print(len(b))
#
# a = {1, 2, 3, 4, 5}
# b = {3, 4, 5, 6, 7}
# c = (a & b - a) | b
# print(c)
#
#
# def join_numbers_from_range(start, stop):
#     d = ''
#     if start == stop:
#         d = str(start)
#     else:
#         for i in range(start, stop + 1):
#             a = str(i)
#             d = d + a
#     return d
#
#
# join_numbers_from_range(1, 5)
#
#
# def my_substr(string, le):
#     i = 0
#     abc = list(string)
#     cde = ''
#     while i < le:
#         cde += abc[i]
#         i += 1
#     return str(cde)
#
#
# string = 'If I look back I am lost'
# print(my_substr(string, 1))  # => 'I'
# print(my_substr(string, 7))  # => 'If I lo'
#
#
# def is_contains_char(text, char):
#     for current_char in text:
#         print(current_char)
#         if current_char.upper() == char.upper():
#             return True
#         else:
#             return False
#
#
# def is_contains_char(text, char):
#     index = 0
#     count = 0
#     while index < len(text):
#         if text[index].upper() == char.upper():
#             # Считаем только подходящие символы
#             count = count + 1
#         # Счетчик увеличивается в любом случае
#         index = index + 1
#     if count == 0:
#         return False
#     else:
#         return True

# def filter_string(text, symbol):
#     abc = symbol.upper()
#     cde = text.upper().replace(abc, '')
#     res_str = cde
#     return res_str
# text = 'If I look forward I win'
# print(filter_string(text, 'i'))  # 'f  look forward  wn'
# print(filter_string(text, 'O'))  # 'If I lk frward I win
a = 10
b = 4
c = 9
d = 3
e = (a - b) * c / d
print(e % 5)
print('aaa')
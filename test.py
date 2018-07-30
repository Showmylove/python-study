#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'elvis08@yeah.net'

import os
import sys
import socket
import math
import functools
import time
import unittest

from PyQt5 import QtWidgets, QtGui
from enum import Enum

print ('hello world')

#name = input('please input your name: ')
#print("hello,", name)

# num = int(input('please input your number: '))
# if num < 0:
#     print(-num)
# else:
#     print(num)

# print('''line1
# line2
# line3''')

# print(r'''hello,\n
# world''')

# a = 123 # a是整数
# print(a)
# a = 'ABC' # a变为字符串
# print(a)

# a = 'ABC'
# b = a
# a = 'XYZ'
# print(b)

# print('包含中文')

# print('%2d-%02d' % (3, 1))
# print('%.2f' % 3.1415926)

# s1 = 72
# s2 = 85
# r = '小明的成绩提高了%.1f%%' %((85-72)/72*100)
# print(r)


# L = [
#     ['Apple', 'Google', 'Microsoft'],
#     ['Java', 'Python', 'Ruby', 'PHP'],
#     ['Adam', 'Bart', 'Lisa']
# ]
# print(L[0][0])
# print(L[1][1])
# print(L[2][2])

# age = 3
# print('your age is', age)
# if age >= 18:
#     print('adult')
# elif age >= 6:
#     print('teenager')
# else:
#     print('kid')

# height = 1.75
# weight = 70.5
# bmi = weight / (height * height)
# if bmi < 18.5:
#     print('过轻')
# elif bmi < 25:
#     print('正常')
# elif bmi < 28:
#     print('过重')
# elif bmi < 32:
#     print('肥胖')
# else:
#     print('严重肥胖')

# names = ['Michael', 'Bob', 'Tracy']
# for name in names:
#     print(name)

# sum = 0
# for x in range(101):
#     sum = sum + x
# print(sum)

# sum = 0
# n = 99
# while n > 0:
#     sum = sum +n
#     n = n - 2
# print(sum)

# Li = ['Bart', 'Lisa', 'Adam']
# for name in Li:
#     print('Hello %s!' %name)

# Li = ['Bart', 'Lisa', 'Adam']
# n = 0
# length = len(Li)
# while n < length:
#     print('Hello %s!' %Li[n])
#     n = n + 1

# n = 1
# while n <= 100:
#     if n > 10:
#         break
#     print(n)
#     n = n + 1
# print('END')

# n = 0
# while n < 100:
#     n = n + 1
#     if n % 2 == 0:
#         continue
#     print(n)
# print('END')

# d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
# print(d['Michael'])

# l1 = ['1', '2', '3']
# l2 = ['4', '5', '6']
# s1 = set(l1)
# print(s1)
# s1.add('4')
# print(s1)
# s1.remove('1')
# print(s1)

# n1 = 255
# n2 = 1000
# print(hex(n1))
# print(hex(n2))

# def my_labs(x):
#     if not isinstance(x, (int, float)):
#         raise TypeError('bad operand type')
#     if x >= 0:
#         return x
#     else:
#         return -x

# print(my_labs(-99))
# print(my_labs(-99.99))

# def move(x, y, step, angle=0):
#     nx = x + step * math.cos(angle)
#     ny = y - step * math.sin(angle)
#     return nx, ny

# x, y = move(100, 100, 60, math.pi / 6)
# print(x, y)

# print(math.sqrt(2))

# def quadratic(a, b, c):
#     if not isinstance(a, (int, float)) & isinstance(b, (int, float)) & isinstance(c, (int, float)):
#         raise TypeError('bad operand type')
#     if a == 0:
#         raise TypeError('bad operand para')
#     deta = b * b - 4 * a * c
#     if deta >= 0:
#         sqrt_deta = math.sqrt(deta)
#         ret1 = (-b + sqrt_deta) / (2 * a)
#         ret2 = (-b - sqrt_deta) / (2 * a)
#         return ret1, ret2
#     else:
#         return None

# # 测试:
# print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
# print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

# if quadratic(2, 3, 1) != (-0.5, -1.0):
#     print('测试失败')
# elif quadratic(1, 3, -4) != (1.0, -4.0):
#     print('测试失败')
# else:
#     print('测试成功')

# def power(x, n=2):
#     s = 1
#     while n > 0:
#         n = n - 1
#         s = s * x
#     return s

# print(power(5))
# print(power(-5, 3))

# def calc(*numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#     return sum

# print(calc(1, 2, 3, 4, 5))
# print(calc(*[1, 2, 3, 4, 5]))

# def product(*args):
#     if len(args) == 0:
#         raise TypeError
#     else:
#         sum = 1
#         for n in args:
#             sum = sum * n
#         return sum

# # 测试
# print('product(5) =', product(5))
# print('product(5, 6) =', product(5, 6))
# print('product(5, 6, 7) =', product(5, 6, 7))
# print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
# if product(5) != 5:
#     print('测试失败!')
# elif product(5, 6) != 30:
#     print('测试失败!')
# elif product(5, 6, 7) != 210:
#     print('测试失败!')
# elif product(5, 6, 7, 9) != 1890:
#     print('测试失败!')
# else:
#     try:
#         product()
#         print('测试失败!')
#     except TypeError:
#         print('测试成功!')

# def fact(n):
#     return fact_iter(n, 1)

# def fact_iter(num, product):
#     if 1 == num:
#         return product
#     return fact_iter(num - 1, num * product)

# print(fact(1))
# print(fact(100))

# def move(n, a, b, c):
#     if 1 == n:
#         print('move', a, '-->', c)
#     else:
#         move(n-1, a, c, b)
#         move(1, a, b, c)
#         move(n-1, b, a, c)

# move(5, 'A', 'B', 'C')

# L = []
# n = 1
# while n < 100:
#     L.append(n)
#     n = n + 2
# print(L)

# L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# print(L[0:3])

# def trim(s):
#     if not s:
#         return s
#     elif ' ' == s[0]:
#         return trim(s[1:])
#     elif ' ' == s[-1]:
#         return trim(s[:-1])
#     else:
#         return s

# def trim(s):
#     if not s:
#         return s
#     l = len(s)
#     n = 0
#     while ' ' == s[n]:
#         n = n + 1
#         if n >= l:
#             break
#     m = -1
#     while ' ' == s[m]:
#         m = m - 1
#         if -m > l:
#             break
#     if -1 == m:
#         m = l
#     else:
#         m = m + 1
#     return s[n:m]

# def trim(s):
#     if not s:
#         return s
#     while ' ' == s[0]:
#         if 1 == len(s):
#             s = ''
#             return s
#         else:
#             s = s[1:]
#     while ' ' == s[-1]:
#         s = s[:-2]
#     return s

# # 测试:
# if trim('hello  ') != 'hello':
#     print('测试失败!')
# elif trim('  hello') != 'hello':
#     print('测试失败!')
# elif trim('  hello  ') != 'hello':
#     print('测试失败!')
# elif trim('  hello  world  ') != 'hello  world':
#     print('测试失败!')
# elif trim('') != '':
#     print('测试失败!')
# elif trim('    ') != '':
#     print('测试失败!')
# else:
#     print('测试成功!')

# d = {'a':1, 'b':2, 'c':3}
# for key, val in d.items():
#     print(key, val)

# def findMinAndMax(L):
#     if not len(L):
#         return (None, None)
#     max = L[0]
#     min = L[0]
#     for n in L:
#         if max < n:
#             max = n
#         if min > n:
#             min = n
#     return(min, max)

# # 测试
# if findMinAndMax([]) != (None, None):
#     print('测试失败!')
# elif findMinAndMax([7]) != (7, 7):
#     print('测试失败!')
# elif findMinAndMax([7, 1]) != (1, 7):
#     print('测试失败!')
# elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
#     print('测试失败!')
# else:
#     print('测试成功!')

# L1 = ['Hello', 'World', 18, 'Apple', None]
# L2 = [s.lower() for s in L1 if isinstance(s, str)]
# # 测试:
# print(L2)
# if L2 == ['hello', 'world', 'apple']:
#     print('测试通过!')
# else:
#     print('测试失败!')

# g = (x * x for x in range(10))
# for n in g:
#     print(n)

# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         print(b)
#         a, b = b, a + b
#         n = n + 1
#     return 'done'

# print(fib(10))

# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield(b)
#         a, b = b, a + b
#         n = n + 1
#     return 'done'

# f = fib(10)
# for n in f:
#     print(n)

# def triangles():
#     L = [1,]
#     while True:
#         yield L
#         # L = L + [0]
#         # L.append(0)
#         # L = [(L[i-1]+L[i]) for i in range(len(L))]
#         L = [1]+[L[i]+L[i+1] for i in range(len(L)-1)]+[1]
#         # length = len(L)
#         # new_L = []
#         # for i in range(length):
#         #     print(L)
#         #     print(L[i-1])
#         #     print(L[i])
#         #     print(L[i-1]+L[i])
#         #     new_L.append(L[i-1]+L[i])
#         #     print(new_L)
#         # L = new_L 
#     return 'done'

# n = 0
# results = []
# for t in triangles():
#     results.append(t)
#     n = n + 1
#     if n == 10:
#         break
# if results == [
#     [1],
#     [1, 1],
#     [1, 2, 1],
#     [1, 3, 3, 1],
#     [1, 4, 6, 4, 1],
#     [1, 5, 10, 10, 5, 1],
#     [1, 6, 15, 20, 15, 6, 1],
#     [1, 7, 21, 35, 35, 21, 7, 1],
#     [1, 8, 28, 56, 70, 56, 28, 8, 1],
#     [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
# ]:
#     print('测试通过!')
# else:
#     print('测试失败!')

# def f(x):
#     return x * x

# r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(list(r))

# def add(x, y):
#     return x + y

# def fn(x, y):
#     return x * 10 + y

# def char2num(s):
#     digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
#     return digits[s]

# print(reduce(fn, [1, 3, 5, 7, 9]))
# print(reduce(fn, map(char2num, '13579')))

# def normalize(name):
#     return name.capitalize()

# # 测试:
# L1 = ['adam', 'LISA', 'barT']
# L2 = list(map(normalize, L1))
# print(L2)

# def prod(L):
#     def multi(x, y):
#         return x * y
#     return reduce(multi, L)

# print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
# if prod([3, 5, 7, 9]) == 945:
#     print('测试成功!')
# else:
#     print('测试失败!')

# def str2float(s):
#     digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
#     def char2int(c):
#         return digits[c]
#     def fn_int(x, y):
#         return x * 10 + y
#     def fn_decimal(x, y):
#         return x * 0.1 + y
#     return reduce(fn_int, map(char2int, s[:s.find('.')])) + reduce(fn_decimal, map(char2int, s[:s.find('.'):-1])) * 0.1

# print('str2float(\'123.456\') =', str2float('123.456'))
# if abs(str2float('123.456') - 123.456) < 0.00001:
#     print('测试成功!')
# else:
#     print('测试失败!')

# def is_odd(n):
#     return 1 == n % 2

# def not_empty(s):
#     return s and s.strip()

# print(list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
# print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))

# def odd_iter():
#     n = 1
#     while True:
#         n = n + 2
#         yield n

# def not_divisible(n):
#     return lambda x: x % n > 0

# def primes():
#     yield 2
#     it = odd_iter()
#     while True:
#         n = next(it)
#         yield n
#         it = filter(not_divisible(n), it)

# for n in primes():
#     if n < 1000:
#         print(n)
#     else:
#         break

# def is_palindrome(n):
#     l1 = list(str(n))
#     l2 = l1[:]
#     l2.reverse()
#     # l2 = l1[::-1]
#     return l1 == l2

# # 测试:
# output = filter(is_palindrome, range(1, 1000))
# print('1~1000:', list(output))
# if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
#     print('测试成功!')
# else:
#     print('测试失败!')

# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

# def by_name(t):
#     x, y = t
#     return x

# def by_score(t):
#     x, y = t
#     return y

# L2 = sorted(L, key=by_name)
# print(L2)

# L3 = sorted(L, key=by_score, reverse = True)
# print(L3)

# def createCounter():
#     a = 0
#     def counter():
#         nonlocal a
#         a = a + 1
#         return a
#     return counter

# # 测试:
# counterA = createCounter()
# print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
# counterB = createCounter()
# if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
#     print('测试通过!')
# else:
#     print('测试失败!')

# def is_odd(n):
#     return n % 2 == 1

# L1 = list(filter(is_odd, range(1, 20)))
# print(L1)

# L2 = list(filter(lambda x: x % 2 == 1, range(1, 20)))
# print(L2)

# def log(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#     return wrapper

# @log
# def now():
#     print('2015-3-15')

# now()
# print(now.__name__)

# def log(text):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kw):
#             print('%s %s():' % (text, func.__name__))
#             return func(*args, **kw)
#         return wrapper
#     return decorator

# @log('execute')
# def now():
#     print('2015-3-15')

# now()
# print(now.__name__)

# def metric(fn):
#     @functools.wraps(fn)
#     def wrapper(*args, **kw):
#         t1 = int(time.time() * 1000)
#         x = fn(*args, **kw)
#         t2 = int(time.time() * 1000)
#         print('%s executed in %s ms' % (fn.__name__, (t2 - t1)))
#         return x
#     return wrapper

# # 测试
# @metric
# def fast(x, y):
#     time.sleep(0.0012)
#     return x + y;

# @metric
# def slow(x, y, z):
#     time.sleep(0.1234)
#     return x * y * z;

# f = fast(11, 22)
# s = slow(11, 22, 33)
# if f != 33:
#     print('测试失败!')
# elif s != 7986:
#     print('测试失败!')
# else:
#     print('测试成功!')

# def log(text):
#     if isinstance(text, str):
#         def withstr(func):
#             @functools.wraps(func)
#             def wrapper(*args, **kw):
#                 print('%s %s():' % (text, func.__name__))
#                 print('begin call: %s()' %func.__name__)
#                 x = func(*args, **kw)
#                 print('end call: %s()' %func.__name__)
#                 return x
#             return wrapper
#         return withstr
#     else:
#         @functools.wraps(text)
#         def withoutstr(*args, **kw):
#             print('begin call: %s()' %text.__name__)
#             x = text(*args, **kw)
#             print('end call: %s()' %text.__name__)
#             return x
#         return withoutstr

# @log
# def now():
#     print('2015-3-15')

# @log('execute')
# def past():
#     print('2015-3-15')

# now()
# past()

# class Student(object):
#     def __init__(self, name, score, gender):
#         self.__name = name
#         self.__score = score
#         self.__gender = gender
#         # set_score(self, score)
#         # set_gender(self, gender)

#     def get_name(self):
#         return self.__name

#     def get_score(self):
#         return self.__score

#     def set_score(self, score):
#         if 0 <= score <= 100:
#             self.__score = score
#         else:
#             raise ValueError('bad score')

#     def set_gender(self, gender):
#         if gender == 'male':
#             self.__gender = gender
#         elif gender ==  'female':
#             self.__gender = gender
#         else:
#             raise ValueError('Please input correct value!')

#     def get_gender(self):
#         return self.__gender

#     def print_name(self):
#         print('%s' % self.__name)

#     def print_score(self):
#         print('%s: %s' % (self.__name, self.__score))

#     def get_grade(self):
#         if self.__score >= 90:
#             return 'A'
#         elif self.__score >= 60:
#             return 'B'
#         else:
#             return 'C'

# # 测试:
# bart = Student('Bart', 99, 'male')
# if bart.get_gender() != 'male':
#     print('测试失败!')
# else:
#     bart.set_gender('female')
#     if bart.get_gender() != 'female':
#         print('测试失败!')
#     else:
#         print('测试成功!')

# class Animal(object):
#     def run(self):
#         print('Animal is running...')

# class Dog(Animal):
#     def run(self):
#         print('Dog is running...')

# class Cat(Animal):
#     def run(self):
#         print('Cat is running...')

# def run_twice(animal):
#     animal.run()
#     animal.run()

# dog = Dog()
# cat = Cat()

# dog.run()
# cat.run()

# run_twice(Animal())
# run_twice(Dog())
# run_twice(Cat())

# class Student(object):
#     count = 0
#     def __init__(self, name):
#         Student.count += 1
#         self.name = name

# # 测试:
# if Student.count != 0:
#     print('测试失败!')
# else:
#     bart = Student('Bart')
#     if Student.count != 1:
#         print('测试失败!')
#     else:
#         lisa = Student('Bart')
#         if Student.count != 2:
#             print('测试失败!')
#         else:
#             print('Students:', Student.count)
#             print('测试通过!')

# class Screen(object):
#     @property
#     def width(self):
#         return self.__width

#     @width.setter
#     def width(self, value):
#         if not isinstance(value, int):
#             raise ValueError('width must be an integer!')
#         if value < 0:
#             raise ValueError('width must greater than 0')
#         self.__width = value

#     @property
#     def height(self):
#         return self.__height

#     @height.setter
#     def height(self, value):
#         if not isinstance(value, int):
#             raise ValueError('__height must be an integer!')
#         if value < 0:
#             raise ValueError('__height must greater than 0')
#         self.__height = value

#     @property
#     def resolution(self):
#         return self.__height * self.__width

# # 测试:
# s = Screen()
# s.width = 1024
# s.height = 768
# print('resolution =', s.resolution)
# if s.resolution == 786432:
#     print('测试通过!')
# else:
#     print('测试失败!')

# Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

# for name, member in Month.__members__.items():
#     print(name, '=>', member, ',', member.value)

# from functools import reduce

# def str2num(s):
#     return float(s)

# def calc(exp):
#     ss = exp.split('+')
#     ns = map(str2num, ss)
#     return reduce(lambda acc, x: acc + x, ns)

# def main():
#     r = calc('100 + 200 + 345')
#     print('100 + 200 + 345 =', r)
#     r = calc('99 + 88 + 7.6')
#     print('99 + 88 + 7.6 =', r)

# main()

# class Student(object):
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#     def get_grade(self):
#         if self.score < 0 or self.score > 100:
#             raise ValueError
#         if self.score < 60:
#             return 'C'
#         if self.score < 80:
#             return 'B'
#         return 'A'

# class TestStudent(unittest.TestCase):

#     def test_80_to_100(self):
#         s1 = Student('Bart', 80)
#         s2 = Student('Lisa', 100)
#         self.assertEqual(s1.get_grade(), 'A')
#         self.assertEqual(s2.get_grade(), 'A')

#     def test_60_to_80(self):
#         s1 = Student('Bart', 60)
#         s2 = Student('Lisa', 79)
#         self.assertEqual(s1.get_grade(), 'B')
#         self.assertEqual(s2.get_grade(), 'B')

#     def test_0_to_60(self):
#         s1 = Student('Bart', 0)
#         s2 = Student('Lisa', 59)
#         self.assertEqual(s1.get_grade(), 'C')
#         self.assertEqual(s2.get_grade(), 'C')

#     def test_invalid(self):
#         s1 = Student('Bart', -1)
#         s2 = Student('Lisa', 101)
#         with self.assertRaises(ValueError):
#             s1.get_grade()
#         with self.assertRaises(ValueError):
#             s2.get_grade()

# if __name__ == '__main__':
#     unittest.main()

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect(('www.sina.com.cn', 80))
# s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
# buffer = []
# while True:
#     # 每次最多接收1k字节:
#     d = s.recv(1024)
#     if d:
#         buffer.append(d)
#     else:
#         break
# s.close()
# data = b''.join(buffer)
# header, html = data.split(b'\r\n\r\n', 1)
# print(header.decode('utf-8'))
# # 把接收的数据写入文件:
# with open('sina.html', 'wb') as f:
#     f.write(html)

# print(sys.argv)
# app = QtWidgets.QApplication(sys.argv)
# windows = QtWidgets.QWidget()
# windows.show()
# sys.exit(app.exec_())

from calc import *

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    windows = QtWidgets.QMainWindow()
    ui = Ui_Frame()
    ui.setupUi(windows)
    windows.show()
    sys.exit(app.exec_())

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import math

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

def product(*args):
    if len(args) == 0:
        raise TypeError
    else:
        sum = 1
        for n in args:
            sum = sum * n
        return sum

# 测试
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')
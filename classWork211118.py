# Chapter07 - Functions and Modules
import math


# def upper_and_lower(s):
#     return s.upper(), s.lower()
#
# word = "Hi there"
#
# print(upper_and_lower(word))

def stars(n):
    return n * '*'


#
# print(stars(10))

# def print_stars(n):
#     print(n * '*')
#
#
# print_stars(10)

def print_centered_in_stars(s):
    line_length = 80
    stars_string = stars(int((line_length - len(s)) / 2))
    print(stars_string + ' ' + s + ' ' + stars_string)


# print_centered_in_stars("CPEN 220")

# def print_mult_table(n = 10, upto=10):
#     for i in range(1, upto + 1):
#         print("%3d * %d = %4d" % (i, n, i * n))


# print_mult_table(5)
# print_mult_table()
# print_mult_table(5, 70)
#
# print(__name__)

# import my_module
# from my_module import print_mult_table
# from my_module import *

# print_mult_table(5, 7)


# Anonymous functions (using the lambda)
# print((lambda x: x ** 2)(5))
print((lambda x, y: x * y)(5, 7))


# The map function -- to be reviewed in Python 3
# map(f, s) applies a function f to all elements of a sequence s
# def f(x):
#     return x ** 2
#
#
# lst = map(f, [1, 2, 3, 4, 5])
# print(lst)


# List comprehension
a = [2, 4, 6, 8]
b = [3 * x for x in a]
c = [3 * x for x in a if x > 4]
d = [[x, 3*x] for x in a]
e = [3 * x for x in range (10) if x % 2 != 0]

names = ['Fady', 'Christine', 'Ali', 'Roy', 'Charbel', 'Chadi']
n = [name for name in ['Christine', 'Ali', 'Boudy', 'Chadi'] if name in names]
print(n)


# Recursion
# def sum(num):
#     if len(num) == 1:
#         return num[0];
#     else:
#         return num[0]+sum(num[1:])
#
# print(sum([1,3]))                 [sum of list]
# def to_string(n,base):
#     converted="0123456789ABCDEF"
#     if n<base:
#         return converted[n]
#     else:
#         return to_string(n//base,base)+converted[n%base]
# print(to_string(2835,16))         [decimal to hexadecimal]
# def list_sum(data):
#     total = 0
#     for element in data:
#         if type(element) == type([]):
#             total +=list_sum(element)
#         else:
#             total+=element
#     return total
# print(list_sum([1,2,[3,4],[5,6]]))            [sum of nested list]
# def factorial(n):
#     if n==0:
#         return 1
#     else:
#         return n*factorial(n-1)
# print(factorial(5))                           [factorial]
# def fibo(n):
#     if n == 2 or n == 1:
#         return 1
#     else:
#         return fibo(n-1)+fibo(n-2)
# print(fibo(10))                               [[fibonacci]
# def sod(n):
#     if n==0:
#         return 0
#     else:
#         return n%10+sod(n//10)
# print(sod(345))                       [sum of digit]
# def sum_series(n):
#     if n<1:
#         return 0
#     else:
#         return n+sum_series(n-2)
# print(sum_series(5))              [sum of series]
# def pwr(a,b):
#     if b==0:
#         return 1
#     elif a==0:
#         return 0
#     elif b==1:
#         return a
#     else:
#         return a*pwr(a,b-1)
# print(pwr(3,4))                   [power base]

# Class
# import array
# for name in array.__dict__:
#     print(name)                   [import build in array]
# def student(student_id,student_name,student_class):
#     return f'Student ID:{student_id}\nStudent Name:{student_name}\nStudent Class:{student_class}'
# print(student('S111','john conner','VI'))
#                                        [using fun attributtes display the names of all arguments]

#1
# def a():
#     return 5
# print(a())

#predict - 5
# correct

#2
# def a():
#     return 5
# print(a()+a())

# #predict - 10
# correct

#3
# def a():
#     return 5
#     return 10
# print(a())

# #predict - 5
# correct

#4
# def a():
#     return 5
#     print(10)
# print(a())

# #predict - 5
# correct

#5
# def a():
#     print(5)
# x = a()
# print(x)

# #predict - 5, undefined
# incorrect - 5, none

#6
# def a(b,c):
#     print(b+c)
# print(a(1,2) + a(2,3))

# #predict - 3, 5, undefined
# incorrect - 3,5, error

#7
# def a(b,c):
#     return str(b)+str(c)
# print(a(2,5))

# #predict - 25
# correct

#8
# def a():
#     b = 100
#     print(b)
#     if b < 10:
#         return 5
#     else:
#         return 10
#     return 7
# print(a())

# #predict - 100, 10
# correct

#9
# def a(b,c):
#     if b<c:
#         return 7
#     else:
#         return 14
#     return 3
# print(a(2,3))
# print(a(5,3))
# print(a(2,3) + a(5,3))

# predict - 7, 14, 21
# correct

#10
# def a(b,c):
#     return b+c
#     return 10
# print(a(3,5))

#predict - 8
# correct

#11
# b = 500
# print(b)
# def a():
#     b = 300
#     print(b)
# print(b)
# a()
# print(b)

# predict - 500, 500, 300, 300
# incorrect - 500, 500, 300, 500 (it appears value reassignments stay within the function and don't change on global scope)

#12
# b = 500
# print(b)
# def a():
#     b = 300
#     print(b)
#     return b
# print(b)
# a()
# print(b)

# predict - 500, 500, 300, 500
# correct

#13
# b = 500
# print(b)
# def a():
#     b = 300
#     print(b)
#     return b
# print(b)
# b=a()
# print(b)

# predict - 500, 500, 300, 300
# correct

#14
# def a():
#     print(1)
#     b()
#     print(2)
# def b():
#     print(3)
# a()

#predict - 1, 3, 2
# correct

#15
# def a():
#     print(1)
#     x = b()
#     print(x)
#     return 10
# def b():
#     print(3)
#     return 5
# y = a()
# print(y)

#predict - 1, 3, 5, 10
# correct



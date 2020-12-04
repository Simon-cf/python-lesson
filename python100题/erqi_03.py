# # 一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
#
# import  math
# for k in range(1, 10000):
#     if (type(math.sqrt(k + 100)) == int) and (type(math.sqrt(k + 100 + 168)) == int):
#         print(k)

# 不能这么做的原因是sqrt()或者**0.5之后得到的结果是一个浮点数， 而且你这是典型的非编程思维，

# 11.8号
# for i in range(2, 85, 2):
#     j = 168 / i
#     if i > j and (i + j) % 2 == 0:
#         n = (i - j) / 2
#         x = n ** 2 -100
#         print(x)


# for i in range(2, 85, 2):
#     j = 168 / i
#     if j % 2 == 0:
#         n = (i - j) / 2
#         x = n ** 2 - 100
#         print(x)


# 11.9号
for i in range(2, 85, 2):
    j = 168 / i # 得到的j不一定是整数
    if j % 2 == 0 and i > j:
        m = (i + j) / 2
        n = (i - j) / 2
        x = n ** 2 - 100
        print(x)



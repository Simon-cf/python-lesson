# 递归中写不了初始值 ， 除非你用能在函数内外都能使用的变量，但有些情况下这样做是不被允许的
# 使用递归
# def fib(num_index):
#     if num_index == 1 or num_index == 2:
#         return 1
#     return fib(num_index - 1) + fib(num_index - 2)
#
#
# print(fib(10))

def fib(num_index):
    if num_index == 1:
        return 0
    elif num_index == 2:
        return 1
    return fib(num_index - 1) + fib(num_index - 2)

print(fib(3))

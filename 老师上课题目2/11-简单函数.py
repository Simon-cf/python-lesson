# 【问题描述】
#
#   编写函数collatz(num)，如果num是偶数，那么collatz()打印出num//2，
#   并返回该值。如果num是奇数，collatz()就打印并返回3*num+1
#
#   然后编写一个程序，由用户输入一个整数，并不断调用collatz()，
#   直到函数返回值为1
#
#
# 【输入形式】
#
#   一个整数
# 【输出形式】
def collatz(num):
    if num == 1:
        return 1
    if num % 2 == 0:
        print(num // 2)
        return collatz(num // 2)
    else:
        print(3 * num + 1)
        return collatz(3 * num + 1)
collatz(3)





#
#   Collatz序列
# 【样例输入】
#
#   3
# 【样例输出】
#
#   10
#
#   5
#
#   16
#
#   8
#
#   4
#
#   2
#
#   1
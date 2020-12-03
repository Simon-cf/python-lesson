# 【问题描述】
#
#   编写一个函数mySum(a,n)，求以下n项式的和：
#
#       s=a+aa+aaa+......+aa...a，  其中a是1~9的数字，
#       最后一项是n位都是a的数字
#
#      程序部分代码如下：
#
#    x,y=eval(input())
#
#    print(mySum(x,y))


def mySum(a, n):
    m = 0
    s = 0
    for i in range(1, n + 1):
        m += a * (10 ** (i - 1))
        s += m
    return s


x, y = eval(input())
print(mySum(x, y))
#
#
#   【输入形式】
#
#   输入a和n的值
# 【输出形式】
#
#   输出s
# 【样例输入】
#
#   1,5
# 【样例输出】
#
#   12345

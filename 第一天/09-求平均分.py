# 【问题描述】编写程序计算学生的平均分。
#
# 【输入形式】输入的第一行表示学生人数n；标准输入的第2至n + 1
# 行表示学生成绩。
# 【输出形式】输出的一行表示平均分（保留两位小数）。
# 若输入的数据不合法（学生人数不是大于0的整数，
# 或学生成绩小于0或大于100），输出“illegal input”。
# 【样例输入】
# 5
# 90
# 91
# 92
# 93
# 94
# 【样例输出】
# 92.00
num = int(input())
s = 0
for i in range(num):
    n = input()
    if type(eval(n)) == int:
        if 0 <= int(n) <= 100:
            pass
        else:
            print("illegal input")
    else:
        print("illegal input")
    s += int(n)
else:
    print("%.2f" % (s / num))

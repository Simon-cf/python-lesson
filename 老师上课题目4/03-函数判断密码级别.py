# 【问题描述】
#
# 输入一个表示密码的字符串，编写程序判断密码的安全级别为低级密码、
# 中级密码和高级密码。
#
#  低级密码要求：
#
#  1. 密码由单纯的数字或字母组成
#
#  2. 密码长度小于等于8位
#
# 中级密码要求：
#
#  1. 密码必须由数字、字母或特殊字符（
#  仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）任意两种组合
#
#  2. 密码长度不能低于8位
#
#  高级密码要求：
#
#  1. 密码必须由数字、字母及特殊字符
#  （仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）三种组合
#
#  2. 密码只能由字母开头
#
#  3. 密码长度不能低于16位
#
# 编写函数判断输入的密码的安全级别，如果为低级密码，
# 则返回"A”；如果如果为中级密码，则返回“B”；如果为高级密码，则返回“C”
#
# def ishave(s,limit)：  判断字符串s中，是否存在limit中任意字符，
# 如果存在，返回1，否则返回0
def ishave(s, limit):
    for i in limit:
        if i not in s:
            return 0
    return 1


# def typenum(psw):   判断psw中存在多少种类别的字符（
# 类别三种，数字，字母，特殊字符 ），返回类别的数量
def typenum(psw):
    count_list = [0, 0, 0]
    for i in psw:
        if i.isdigit():
            count_list[0] = 1
        elif i.isalpha():
            count_list[1] = 1
        else:
            count_list[-1] = 1
    return sum(count_list)


#
# def safe(psw): 判断psw的安全性，返回安全级别对应的字符
def safe(psw):
    count = typenum(psw)
    s = ''
    for i in psw:
        if not i.isalnum():
            s += i
    if len(psw) <= 8 or psw.isalnum():
        return "A"
    elif len(psw) >= 16 and count == 3 and psw[0].isalpha() and ishave("~!@#$%^&*()_=-/,.?<>;:[]{}|\\", s):
        return "C"
    else:
        return "B"


x = input()
print(safe(x))
#
# 【输入形式】
#
#         一个表示密码的字符串，可以是字母、数字或题目中所示特殊字符
#
# 【输出形式】
#
#         A 或 B 或 C
#
# 【样例输入】
#
#         wer123456#$%
#
# 【样例输出】
#
#         B
# 【样例说明】
# 【评分标准】

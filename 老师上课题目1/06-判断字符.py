# 【问题描述】已知变量ch中存放了一个字符,判断该字符是字母字符、
# 数字字符还是其他字符。
#
# 【输入形式】
#
# 只输入一个字符
ch = input("please input a char:")

# 【输出形式】
if ch.isalpha():
    print("alphabet character")
elif ch.isdigit():
    print("digital character")
else:
    print("others character")
# alphabet character或者digital character或者others character
#
# 【样例输入】
#
# please input a char:c
#
# 【样例输出】
#
# alphabet character
#
# 【样例说明】
#
# 样例输入中的下划线表示具体输入的字符。
# 【评分标准】
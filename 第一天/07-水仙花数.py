# 	判断一个3位数是否是水仙花数。
# 【问题描述】输入一个三位正整数abc，如果满足a^3+b^3+c^3=abc，
# 则该数是水仙花数。例如123不等于1+8+27所以123不是水仙花数。
# 【输入形式】
#
# 输入一个三位正整数
# 【输出形式】
num = int(input("please input a three-digit number:"))
if 100 <= num <= 999:
    if (num // 100) ** 3 + (num % 100 // 10) ** 3 + (num % 10) == num:
        print("true")
    else:
        print("false")
else:
    print("error")
# false或者true或者error
# 【样例输入】
#
# please input a three-digit number: 123
#
# 【样例输出】
#
# false
# 【样例说明】
#
# 样例输入中的下划线表示具体输入的数字；需要增加范围检测，
# 当你输入的不是三位数时，输出error。
# 【评分标准
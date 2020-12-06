# 给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
n = input()
print(len(n))
for i in n[::-1]:
    print(i, end=" ")

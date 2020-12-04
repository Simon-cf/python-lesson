# 【问题描述】
#
# 请编写程序，生成随机密码。具体要求如下：
import random
random.seed(10)
n = int(input())
s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
pswd = ''
for i in range(n):
    pswd += s[random.randint(0, len(s))]
else:
    print(pswd)
print((3, 5) + (2, 1))
#
#     （1）使用 random 库，采用 10作为随机数种子。
#
# 提示：random.seed(10)
#
#     （2）密码允许字符如下：
#
#s="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
#
#     （3）密码长度为输入的数字。
#
# 【样例输入】
#
# 5
# 【样例输出】
#
# KcBEK
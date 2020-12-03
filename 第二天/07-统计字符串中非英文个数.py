# 【问题描述】统计字符串s中非英文字母的个数并输出。
#
# 【输入形式】字符串s
#
# 【输出形式】非英文字母的个数
#
# 【输入示例】a1b2
s = input()
count = 0
for i in s:
    if i.isalpha():
        count += 1
else:
    print(count)
# 【输出示例】2
# 【问题描述】
#
# 给定n个整数，请统计出每个整数出现的次数，按出现次数从多到少的顺序输出。
#
#
# 【输入形式】
#
# 第一行包含一个整数n，表示给定数字的个数; 第二行包含n个整数，相邻的整数之间用一个空格分隔，表示所给定的整数。
#
# 【输出形式】
n = int(input())
n_list = list(map(int, input().split()))
n_dict = {}
for i in n_list:
    if i in n_dict.keys():
        n_dict[i] += 1
    else:
        n_dict[i] = 1
k_list = []
for v in sorted(n_dict.values(), reverse=True):
    for k in sorted(n_dict.keys()):
        if n_dict[k] == v and k not in k_list:
            print(k, v)
            k_list.append(k)

# 输出有多行，每行包含两个整数，分别表示一个给定的整数和它出现的次数。按出现次数递减的顺序输出。如果两个整数出现的次数一样多，则先输出值较小的，然后输出值较大的。
#
# 【样例输入】
#
# 12
#
# 5 2 3 3 1 3 4 2 5 2 3 5
#
# 【样例输出】
#
# 3 4
#
# 2 3
#
# 5 3
#
# 1 1
#
# 4 1

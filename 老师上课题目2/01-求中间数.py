# 求中间数
# 【问题描述】
#
# 　　在一个整数序列a1, a2, …, an中，如果存在某个数，
# 大于它的整数数量等于小于它的整数数量，则称其为中间数。
# 在一个序列中，可能存在多个下标不相同的中间数，这些中间数的值是相同的。
#
# 　　给定一个整数序列，请找出这个整数序列的中间数的值。
#
# 【输入形式】
#
# 　　输入的第一行包含了一个整数n，表示整数序列中数的个数。
#
# 　　第二行包含n个正整数，依次表示a1, a2, …, an。

# n = int(input())
# n_list = []
# num_list = []
# for i in range(n):
#     num = int(input())
#     n_list.append(num)
# for k in sorted(n_list):
#     if len(sorted(n_list)[:sorted(n_list).index(k)]) == \
#             len(sorted(n_list, reverse=True)
#                 [:sorted(n_list, reverse=True).index(k)]):
#         if k not in num_list:
#             print(k)
#             num_list.append(k)
# if not num_list:
#     print(-1)

# n = int(input())
# n_list = []
# for i in range(n):
#     num = int(input())
#     n_list.append(num)
#
# low_count = 0
# high_count = 0
# num_list = []
# for k in n_list:
#     for m in n_list:
#         if m < k:
#             low_count += 1
#         elif m > k:
#             high_count += 1
#
#     if low_count == high_count:
#         if k not in num_list:
#             print(k)
#             num_list.append(k)
#     low_count = 0
#     high_count = 0
#
# if not num_list:
#     print(-1)


# 【输出形式】
#
# 　　如果约定序列的中间数存在，则输出中间数的值，否则输出 - 1
# 表示不存在中间数。
#
# 【样例输入】
#
# 　　6
#
# 　　2
# 6
# 5
# 6
# 3
# 5
#
# 【样例输出】
#
# 　　5
#
# 【样例说明】
#
# 　　比5小的数有2个，比5大的数也有2个。
#
#
#
# 【样例输入】
#
# 　　4
#
# 　　3
# 4
# 6
# 7
#
# 【样例输出】
#
# 　　-1
#
# 【样例说明】
#
# 　　在序列中的4个数都不满足中间数的定义。
#
# 【样例输入】
#
# 　　5
#
# 　　3
# 4
# 6
# 6
# 7
#
# 【样例输出】
#
# 　　-1
#
# 【样例说明】
#
# 在序列中的5个数都不满足中间数的定义。
#

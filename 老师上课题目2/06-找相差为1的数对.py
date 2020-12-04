# 	找相差为1的数对
# 【问题描述】
#
# 　　给定n个不同的整数，问这些数中有多少对整数，它们的值正好相差1。
#
# 【输入形式】
#
# 　　输入的第一行包含一个整数n，表示给定整数的个数。
#
# 　　第二行包含所给定的n个整数。
#
# 【输出形式】
#
# 　　输出一个整数，表示值正好相差1的数对的个数。
n = int(input())
n_list = list(map(int, input().split()))
count = 0
Lst = []
for i in n_list:
    for k in n_list[n_list.index(i) + 1:]:
        if abs(i - k) == 1:
            count += 1
            Lst.append((i, k))
print(count)
for m in Lst:
    print(m[0], m[1])

# 【样例输入】
#
# 　　6
#
# 　　10 2 6 3 7 8
#
# 【样例输出】
#
#       3
#
#   2 3
#
#       6 7
#
#       7 8
#
# 【样例说明】
#
# 　　值正好相差1的数对包括(2, 3), (6, 7), (7, 8)。
#

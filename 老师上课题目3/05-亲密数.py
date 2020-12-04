# 【问题描述】
#
#  求整数n以内（含n）的全部亲密数。
#
# 说明：如果正整数；
# 且正整数B的全部因子(包括1，不包括B本身)之和等于A，A不等于B，
# 则将正整数A和B称为亲密数。
#
# 1不和其他数形成亲密数。
#
# 编写函数sumElem()，实现统计一个数字的因子之和(包括1，不包括A本身)
def semElem(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    return sum

n = int(input())
# for i in range(2, n + 1):
#     for k in range(i + 1 , n + 1):
#         if semElem(i) == k and semElem(k) == i:
#             print(i, k)
for i in range(2, n + 1):
    B = semElem(i)
    if semElem(B) == i and B != i:
        if i > B:
            continue
        print(i, B)


# 【输入形式】
#
# 输入整数n
# 【输出形式】
#
#  每一行输出一对亲密数，中间用一个空格隔开。
#
#  每一对亲密数只输出一次，小的在前。
#
#  各对亲密数按序排序，按亲密数中小的那个数从小到大排序。
#
# 【样例输入】
#
# 3000
#
# 【样例输出】
#
# 220 284
#
# 1184 1210
#
# 2620 2924

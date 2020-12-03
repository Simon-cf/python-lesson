# 【问题描述】

# 输入一组数到列表nums，
# 请找到列表中任意两个元素相加能够等于9的元素
# 形成一个元组，使其小数在前大数在后，如：(2,7), (1,8)。
# 重复的元组元素只保留一个，结果按元组第一个元素从小到大顺序输出。
#
# 【样例输入】
Lst = []
nums_list = list(map(int, input("numbers:").split(',')))
for i in nums_list:
    for k in nums_list:
        if k + i == 9:
            if tuple(sorted((k, i))) not in Lst:
                Lst.append(tuple(sorted((k, i))))
print(sorted(Lst))


# numbers:3,4,5,7,2,8,1
#
# 【样例输出】
#
# [(1, 8), (2, 7), (4, 5)]
#
# 【难点解析】可以一开始定义一个空列表Lst，
# 然后每次将符合要求的，例如Lst.append((1,8))追加一个元组的方式
# （看清楚里面(1,8)的写法），把元组作为列表的元素插入列表。


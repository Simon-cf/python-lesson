#
# 【问题描述】
#
#   编写一个函数isRepeated(v)，用于判断一个列表中的元素是否存在重复，若有重复则返回True，  否则返回False
#
#   完成完整代码。
#
#
# 【输入形式】
#
#   列表
# 【输出形式】
#
#   True或False
# 【样例输入】
#
#   [1,2,3,2,5]
# 【样例输出】
#
#   True
# 【样例说明】
# 【评分标准】
#
def isRepeated(v):
    if len(set(v)) < len(v):
        return True
    return False


list1 = eval(input('>'))
print(isRepeated(list1))

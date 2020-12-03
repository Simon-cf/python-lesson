# 	餐厅服务评价
# 【问题描述】假设有10个学生被邀请来给餐厅的饮食和服务质量打分，
# 分数划分为1~9这9个等级(1表示最低分，9表示最高分)
# 编程统计输出餐饮服务质量调查结果。

# 【输入形式】输入1行，输入10个1到9之间的整数，
# 每个整数之间以空格为分隔符
#
# 【输出形式】输出9行，每行两个数（以空格为分隔符），
# 一个为1到9之间的整数，表示等级；一个为这个等级对应的票数。
n_list = list(map(int, input().split()))

scores_dict = {}
for i in range(9):
    scores_dict[i + 1] = 0
print(scores_dict)
for n in n_list:
    if n not in scores_dict.keys():
        scores_dict[n] = 1
    else:
        scores_dict[n] += 1


for k, v in sorted(scores_dict.items()):
    print(k, v)

# 【样例输入】
#
#         1 2 3 3 3 2 2 7 8 9
#
# 【样例输出】
#
#         1 1
#
#         2 3
#
#         3 3
#
#         4 0
#
#         5 0
#
#         6 0
#
#         7 1
#
#         8 1
#
#         9 1
#
# 【样例说明】
# 【评分标准】
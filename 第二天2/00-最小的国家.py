# 【问题描述】输入5个国名，编程实现按字典序排序并输出排在最前面的国家名。
#
# 【输入形式】5行，每行输入一个国家的英文名字
country = {

}
for i in range(5):
    country_name = input()
    country[country_name] = country_name
print(sorted(country)[0])
# 【输出形式】一行，字典序最小的国家的英文名字
#
# 【样例输入】
#
#         China
#
#         America
#
#         Japan
#
#         England
#
#         Korea
#
# 【样例输出】
#
#         America
#
# 【样例说明】
# 【评分标准】
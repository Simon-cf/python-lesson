# 【问题描述】
#
#   编写函数isLeap(year)用于判断year是否是闰年，若是闰年则返回True，否则返回False。
#
#   编写函数days(year,month)用于计算year所在的month的天数，days(year,month)函数需要调用isLeap()函数以帮助判断2月份的天数（year若不是闰年，返回28，否则返回29） 要求程序能根据用户输入的日期，计算该日期是这一年的第几天。
#
# 【输入形式】
#
#   输入某个日期（格式为year/month/day)
# 【输出形式】
#
#   该日期是一年的第几天
# 【样例输入】
#
#   2019/3/18
# 【样例输出】
#
#   77
# 【样例说明】
# 【评分标准
def isLeap(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    return False

def days(*args):
    days_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if isLeap(args[0]):
        days_list[1] = 29
    return sum(days_list[:args[1] - 1]) + args[2]

date_tuple = tuple(map(int, input().split('/')))
print(days(*date_tuple))

date_list = list(map(int, input("请分别输入年月日，并用空格隔开").split()))
month_days = []
year, month, day = date_list[0], date_list[1], date_list[2]
# 用循环向列表中追加每个月的天数
for i in range(1, 13):
    # 1.判断是否是闰年并且是否轮到追加二月的天数
    if i == 2:
        if ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
            month_days.append(29)
        else:
            month_days.append(28)
    elif i in [1, 3, 5, 7, 8, 10, 12]:
        month_days.append(31)
    else:
        month_days.append(30)

days = sum(month_days[:month - 1]) + day
print("It's the %sth day in %s" % (days, year))


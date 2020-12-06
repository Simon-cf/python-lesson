import datetime


print(datetime.date.today())

# 创建时间对象
time = datetime.date(2020, 12, 6)
print(time)
# strftime()修改格式
print(time.strftime("%d/%m/%Y"), )
time = time + datetime.timedelta((1))
print(time)
print(time.day)
# 日期替换
time = time.replace(day=1)
print(time)
time = time.replace(year=1999)
print(time)

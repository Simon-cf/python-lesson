# 古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，
# 小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
# 把三个月之后每个月生一个兔子封装成一个方法
def give_birth(months_left):
    if months_left < 4:
        return 2
    return give_birth(months_left - 1) + 2

print(give_birth(7))



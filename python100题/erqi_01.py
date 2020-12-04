# 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
count = 0
for k_0 in range(1, 5):
    for k_1 in range(1, 5):
        if k_1 == k_0:
            continue
        for k_2 in range(1, 5):
            if k_2 == k_1 or k_2 == k_0:
                continue
            count += 1
            print(k_0, end="")
            print(k_1, end="")
            print(k_2, end="")
            print()
print(count)

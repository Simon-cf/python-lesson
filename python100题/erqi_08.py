# 输出 9*9 乘法口诀表。

for k in range(1, 10):
    for j in range(1, k + 1):
        print("%s*%s=%s" % (j, k, k * j), end="\t")
    print()



# 1
# 1 1
# 1 2 1
# 1 3 3  1
# 1 4 6  4  1
# 1 5 10 10 5   1
# 1 6 15 20 15  6   1
# 1 7 21 35 35  21  7  1
# 1 8 28 56 70  56  28 8  1
# 1 9 36 84 126 126 84 36 9 1
k_list = [[1] * i for i in range(1, 11)]
for n in range(len(k_list)):
    if len(k_list[n]) >= 3 and n > 1:
        for m in range(1, len(k_list[n]) - 1):
            k_list[n][m] = k_list[n - 1][m] + k_list[n - 1][m - 1]
for k_ in k_list:
    for k in k_:
        print(str(k).center(4),end="")
    print()


# 冒泡排序
n_list = list(map(int, input().split()))

for i in range(1, len(n_list)):
    if n_list[i] > n_list[i - 1]:
        n_list[i], n_list[i - 1] = n_list[i - 1], n_list[i]
print(n_list)

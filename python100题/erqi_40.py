n_list = list(map(int, input().split()))

for i in range(len(n_list) // 2):
    n_list[i], n_list[-(1 + i)] = n_list[-(1 + i)], n_list[i]
print(n_list)

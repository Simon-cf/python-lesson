import math

n_list = list(map(int, input().split()))

n_list[0], n_list[n_list.index(max(n_list))] = n_list[n_list.index(max(n_list))], n_list[0]

n_list[-1], n_list[n_list.index(min(n_list))] = n_list[n_list.index(min(n_list))], n_list[-1]
print(n_list)

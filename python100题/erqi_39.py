# 有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。
n_list = [4222,65,6,2,0]
k = int(input())
for n in n_list:
    if n_list[0] <= n_list[-1]:
        if n > k:
            n_list.insert(n_list.index(n), k)
            break
    else:
        if n < k:
            n_list.insert(n_list.index(n), k)
            break
print(n_list)

# 有 n 个整数，使其前面各数顺序向后移 m 个位置，最后 m 个数变成最前面的 m 个数
n_list = list(map(int, input().split()))
m = int(input())
n_list = n_list[-m:] + n_list[:-m]
print(n_list)

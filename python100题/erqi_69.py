# 有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数）
# ，凡报到3的人退出圈子，问最后留下的是原来第几号的那位。
n = int(input())
n_list = [i for i in range(1, n + 1)]
print(n_list)
k_list = []
count = 0
m = 0
while True:
    count += 1

    if count % 3 != 0:
        k_list.append(n_list[m])
    m += 1
    if m == len(n_list):
        n_list = k_list
        k_list = []
        m = 0
    if len(n_list) < 2:
        print(n_list[0])
        break
    # if k_list.count(n_list[]) == 2:
    #     k_list.remove(n_list[m - 1])
    #     n_list = k_list
    #     k_list = []
    #     m = 0
    # if len(n_list) < 2:
    #     print(n_list[0])
    #     break

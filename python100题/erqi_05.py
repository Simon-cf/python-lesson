# 输入三个整数x,y,z，请把这三个数由小到大输出。
n_list = list(map(int, input("请输入三个整数，并用空格分隔开").split()))
for k in sorted(n_list):
    print(k, end=" ")

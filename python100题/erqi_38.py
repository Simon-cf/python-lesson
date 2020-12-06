n_list = []
for i in range(3):
    n_list_ = []
    for k in range(3):
        n_list_.append(int(input("input num:")))
    else:
        n_list.append(n_list_)
sum = 0
for i in range(3):
    sum += n_list[i][i]
print(sum)



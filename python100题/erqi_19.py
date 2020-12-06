for i in range(1, 1001):
    k_list = []
    for k in range(1, i):
        if i % k == 0:
            k_list.append(k)

    else:
        if sum(k_list) == i:
            print(i)
            for m in k_list:
                print(m, end=" ")
            print()




n_list1 = list(map(int, input().split()))
n_list2 = list(map(int, input().split()))
count = 0
for i in n_list1:
    for k in n_list2:
        if i == k:
            count += 1
print(count)
m = 1
n = 2
sum_list = [n / m]
for i in range(1, 20):
    temp = n
    n += m
    m = temp
    sum_list.append(n / m)
print(sum_list)
print(sum(sum_list))

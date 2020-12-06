n = int(input())
m = n
k_list = []
while True:
    for k in range(2, round(m ** 0.5) + 1):
        if n % k == 0:
            k_list.append(k)
            n = n // k
            break
    else:
        break
print("m = ", end='')
for i in k_list[:-1]:
    print("{} * ".format(i), end='')
print(k_list[-1])
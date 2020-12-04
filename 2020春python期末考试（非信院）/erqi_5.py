import os

Lst = []
num = 0
max = 0
n_list = sorted(list(map(int, input().split())))

for i in range(1, len(n_list)):
    if n_list[i] > num:
        count = 0
        if n_list[i] == n_list[i - 1] + 1:
            Lst.append([n_list[i - 1], n_list[i]])

            while True:
                count += 1
                if i + count >= len(n_list):
                    break
                if n_list[i + count] == n_list[i + count - 1] + 1:
                    Lst[len(Lst) - 1].append(n_list[i + count])
                else:
                    num = Lst[len(Lst) - 1][-1]
                    break

for k_list in Lst:
    if max < len(k_list):
        max = len(k_list)

fp = open('out.txt', 'w', encoding='utf-8')
fp.write(str(max) + '\n')
for k_list in Lst:
    if len(k_list) == max:
        for k in k_list:
            fp.write(str(k) + ' ')
        else:
            fp.write('\n')

# 3520 4 3 89 56 88 3521 9 90 1 99 2 87

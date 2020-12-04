import random

even_count = 0
odd_count = 0
random.seed(10)
n = int(input("n:"))
n_list = []
for i in range(n):
    n_list.append(random.randint(1, 100))

for k in n_list:
    if k % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
else:
    if odd_count > even_count:
        print("odd")
    else:
        print("even")

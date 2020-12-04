import random

random.seed(10)
n_list = []
n = int(input("n:"))
for i in range(n):
    n_list.append(random.randint(100, 200))
for k in sorted(n_list):
    print(k)

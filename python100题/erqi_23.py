num = int(input())
for i in range(1, num + 1):
    print("{:^{}}".format("*" * (2 * i - 1), 2 * num - 1))
for k in range(1, num):
    print("{:^{}}".format("*" * (2 * (num - k) - 1), 2 * num - 1))

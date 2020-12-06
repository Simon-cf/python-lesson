days = int(input())
k = 0
for i in range(days - 1):
    k += 2 ** i * 3
print(k + 1)

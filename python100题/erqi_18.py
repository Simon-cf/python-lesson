s = 0
n = int(input())
a = int(input())
s_a = 0
for i in range(1, n + 1):
    s_a += a * 10 ** (i - 1)
    s += s_a
print(s)

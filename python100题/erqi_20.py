height = 100
times = 10
s = 100
m = 0
for n in range(1, times + 1):
    m = height * 0.5 ** n
    s += 2 * m

print(s)
print(m)

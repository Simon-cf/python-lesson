a = 2
b = 9
a, b = b, a
print(a, b)

a = a + b
b = a - b
a = a - b
print(a, b)

temp = a
a = b
b = temp
print(a, b)
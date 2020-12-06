s = input()
a_count = 0
d_count = 0
s_count = 0
o_count = 0
for i in s:
    if i.isalpha():
        a_count += 1
    elif i.isdigit():
        d_count += 1
    elif i.isspace():
        s_count += 1
    else:
        o_count += 1
print(a_count, s_count, d_count, o_count)



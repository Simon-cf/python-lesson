s = input()
a_count = 0
d_count = 0
s_list = []
count = 0
s_new = ''

for i in s:
    if i.isalpha():
        a_count += 1
    if i.isdigit():
        d_count += 1

for k in s:
    if k.isalpha():

        s_new += k
    else:
        k = " "
        s_new += k



print(d_count)
print(a_count)
print(len(s_new.split()))
for m in s_new.split():
    print(m, end=" ")


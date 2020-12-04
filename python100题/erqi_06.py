# 斐波那契数列。
num, num_index = eval(input("请输入你想得到的斐波那契数列的长度和想得到的数列中数字的位数"))
num_list = []
for i in range(num):
    if i > 1:
       num_list.append(num_list[i - 2] + num_list[i - 1])
    else:
        num_list.append(i)

print(num_list)
print(num_list[num_index - 1])
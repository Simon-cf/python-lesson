s = input("please input a number:")
n_list = [int(i) for i in s]
if 36 <= sum(n_list) <= 45:
    print("yes")
else:
    print("no")

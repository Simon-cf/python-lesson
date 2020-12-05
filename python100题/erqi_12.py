count = 0
for i in range(101, 200):
    for k in range(2, i):
        if i % k == 0:
            break
    else:
        print(i)
        count += 1
print("the total is {}".format(count))

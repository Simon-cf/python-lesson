for i in range(1, 100):
    for k in range(2, i):
        if i % k == 0:
            break
    else:
        print(i)

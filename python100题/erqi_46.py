while True:
    n = int(input("Please enter a number:"))
    if n ** 2 < 50:
        print(n ** 2)
        break
    print("结果为{}".format(n ** 2))

def midNum(n):
    average = sum(n) / len(n)
    if len(n) % 2 == 0:
        middle = (n[len(n) // 2 ]+ n[len(n) // 2 - 1]) / 2
    else:
        middle = n[len(n) // 2]
    return "{:.2f}".format(average), middle


n = sorted(list(eval(input())))
print(midNum(n)[0])
print(midNum(n)[1])


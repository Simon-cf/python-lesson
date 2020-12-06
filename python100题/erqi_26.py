def get_mutiple(num):
    if num == 1:
        return 1
    return num * get_mutiple(num - 1)
print(get_mutiple(5))
def get_mutiple(num):
    if num == 1:
        return 1
    return num * get_mutiple(num - 1)


def get_add(num):
    if get_mutiple(num) == 1:
        return 1
    result = get_mutiple(num)
    return result + get_add(num - 1)
print(get_add(20))

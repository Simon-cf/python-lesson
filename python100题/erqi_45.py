def get_add(num):
    if num == 1:
        return 1
    return get_add(num - 1) + num

print(get_add(100))
def get_add(num):
    if num == 1 or num == 2:
        return 1 / num
    return get_add(num - 2) + 1 / num
print(get_add(6))
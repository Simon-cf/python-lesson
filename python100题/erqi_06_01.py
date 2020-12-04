def feb(num_index):
    """得到斐波那契数列的指定位置对应的数字"""
    a, b = 0, 1
    for i in range(num_index - 1):
        a, b = b, a + b
    return a
print(feb(1))






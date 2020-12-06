def rev_list(list_):
    if len(list_) == 1:
        print(list_[0])
        return
    print(list_.pop(-1))
    rev_list(list_)


rev_list([1, 2, 3, 4, 5])

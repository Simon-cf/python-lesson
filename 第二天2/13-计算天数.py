def isLeap(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    return False

def days(*args):
    days_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if isLeap(args[0]):
        days_list[1] = 29
    return sum(days_list[:args[1] - 1]) + args[2]

date_tuple = tuple(map(int, input().split('/')))
print(days(*date_tuple))

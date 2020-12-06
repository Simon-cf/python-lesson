week = {
    "Monday": 1,
    "Tuesday": 2,
    "Wednesday": 3,
    "Thursday": 4,
    "Friday": 5,
    "Saturday": 6,
    "Sunday": 7
}

n = input()
k_list = []
for k in week.keys():
    if n == k[0]:
        k_list.append(k)
else:
    if len(k_list) > 1:
        m = input()
        for k_ in k_list:
            if m == k_[1]:
                print(k_)
    else:
        print(k_list[0])

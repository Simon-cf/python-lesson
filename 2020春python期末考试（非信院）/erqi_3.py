s_ID_list = []
while True:
    s_ID = input()
    if not s_ID:
        break
    s_ID_list.append(s_ID)

code_dict = {
    '01': 'CPST',
    '02': 'CAS',
    '03': 'CRE',
    '04': 'CLST',
    '05': 'CHFS',
    '06': 'EMC',
    '07': 'CET',
    '08': 'CF',
    '09': 'CFST',
    '10': 'CS'
}
nums_dict = {

}

for ID in s_ID_list:
    if ID[5:7] in nums_dict.keys():
        nums_dict[ID[5:7]] += 1
    else:
        nums_dict[ID[5:7]] = 1


k_list = []
for v in sorted(nums_dict.values()):
    if v != 0:
        for k in nums_dict.keys():
            if nums_dict[k] == v:
                if k not in k_list:
                    print(code_dict[k], v)
                    k_list.append(k)

# 能否用字典排序简化这里的代码
# ——> 学一下字典的排序（根据值排序）
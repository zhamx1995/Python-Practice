def sort(data):
    dict = {}
    list = []
    for item in data:
        if dict.has_key(item):
            prev = dict[item]
            dict[item] = prev + 1
        else:
            dict[item] = 1
            list.append(item)
    list.sort(cmp=lambda x,y: customSort(x,y,dict), reverse=False)
    return list

def customSort(x,y,dict):
    if dict[x] == dict[y]:
        return cmp(x,y)
    else:
        return dict[y] - dict[x]

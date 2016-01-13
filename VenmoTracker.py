def networth(transactions):
    dict = {}
    result = []
    for tran in transactions:
        temp = tran.split(":")
        if dict.has_key(temp[0]):
            val = dict[temp[0]] - temp[2]
            dict[temp[0]] = val
        else:
            dict[temp[0]] = -temp[2]
        if dict.has_key(temp[1]):
            val = dict[temp[1]] + temp[2]
            dict[temp[1]] = val
        else:
            dict[temp[1]] = temp[2]
    else:
        for key in dict.keys():
            st = key+":"+str(dict[key])
            result.append(st)
        else:
            result.sort(key=None, reverse=False)
            return result
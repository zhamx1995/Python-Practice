def emailsLargest(courses):
    dict = {}
    for data in courses:
        st = data.split(":")
        if dict.has_key(st[0]):
            val = dict[st[0]]
            val.append(st[2])
            dict[st[0]] = val
        else:
            val = []
            val.append(st[2])
            dict[st[0]] = val
    else:
        max = 0
        list = []
        for key in dict.keys():
            if len(dict[key]) > max:
                list = []
                list.append(key)
                max = len(dict[key])
            if len(dict[key]) == max:
                list.append(key)
        list.sort()
        result = dict[list[0]]
        result.sort()
        val = ""
        for email in result:
            val += email + " "
        val = val[:-1]
        return val
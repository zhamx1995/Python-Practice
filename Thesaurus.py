def edit(entry) :
    entryList = []
    for one in entry:
        entryList.append(one.split(" "))
    for times in range(0,10):
        nochanged = True
        for m in range(0, len(entryList)):
            for n in range(0, len(entryList)):
                if m<len(entryList) and n<len(entryList) and m!=n:
                    nval = entryList[n]
                    mval = entryList[m]
                    common = numInCommon(nval, mval)
                    if common >= 2:
                        entryList.append(union(nval, mval))
                        entryList.remove(nval)
                        entryList.remove(mval)
                        nochanged = False
        if nochanged:
            break
    result = []
    for list in entryList:
        list.sort()
        temp =""
        for item in list:
            temp += item + " "
        temp = temp[:-1]
        result.append(temp)
    result.sort()
    return result

def numInCommon(a, b):
    common = 0
    for ai in a:
        for bi in b:
            if ai == bi:
                common += 1
    return common

def union(a,b):
    u = a
    for bitem in b:
        if bitem not in u:
            u.append(bitem)
    return u
                    
    
def pcount(low,high):
    primeList = [2]
    result = 0
    for num in range(3, high):
        for index in range(0, len(primeList)):
            if num%primeList[index] == 0:
                break
            if pow(primeList[index],2)>num:
                primeList.append(num)
                if num>=low:
                    result += 1
                break
        else:
            primeList.append(num)
            if num>=low:
                result += 1
    else:
        if low == 1:
            result += 1
        return result
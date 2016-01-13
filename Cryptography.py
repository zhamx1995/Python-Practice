def encrypt(numbers) :
    list = []
    for num in numbers:
        list.append(encode(num,numbers))
    else:
        list.sort(key=None, reverse=True)
        return long(list[0])

def encode(num, numbers):
    result = num+1
    for one in numbers:
        result *= one
    else:
        result /= num
        return result
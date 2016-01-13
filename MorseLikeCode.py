def decrypt(library,message):
    result = ""
    msgs = message.split()
    dict = {}
    for lib in library:
        datas = lib.split()
        dict[datas[1]] = datas[0]
    else:
        for index in range(0, len(msgs)):
            if dict.has_key(msgs[index]): 
                result += dict.get(msgs[index])
            else:
                result += "?"
        else:
            return result
def decode(cipher, shift):
    result = ""
    for index in range(0, len(cipher)):
        asc = ord(cipher[index]) - shift
        if asc<65:
            asc += 26
        result += chr(asc)
    else:
        return result
def repeat(word, number):
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    result = ""
    if word[0] in vowels:
        result = word
    elif len(word)>2:
        if word[2] in vowels:
            result = word[0:3]*(number-1) + word
        elif word[1] in vowels:
            result = word[0:2]*(number-1) + word
        else:
            result = word
    elif len(word)>1:
        if word[1] in vowels:
            result = word[0:2]*(number-1) + word
        else:
            result = word
    else:
        result = word
    result = result.lower()
    if word[0].isupper():
        return result.capitalize()
    else:
        return result
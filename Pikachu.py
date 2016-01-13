def check(word):
    while len(word) > 0:
        if word.startswith("pi"):
            word = word[2:]
        elif word.startswith("ka"):
            word = word[2:]
        elif word.startswith("chu"):
            word = word[3:]
        else:
            return "NO"
    return "YES"
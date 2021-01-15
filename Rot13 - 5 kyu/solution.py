def rot13(message):
    print(message)
    alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    res = ""
    for c in message:
        if c.lower() in alphabet:          
            if c.isupper():
                res+= alphabet[alphabet.index(c.lower())+13].upper()
            else:
                res+= alphabet[alphabet.index(c)+13]
        else:
            res+=c
    return res

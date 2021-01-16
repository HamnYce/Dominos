
def alphabet_position(text):
    l = ""
    for letter in text:
        unic = ord(letter.lower())
        if (97 <= unic <= 122):
            l += str(unic-96) + " "
    
    return l.strip()




print(alphabet_position("The sunset sets at twelve o' clock."))

#someone's OP one liner
# text = "The sunset sets at twelve o' clock."
# for x in text:
#     print(str(ord(x.lower())-96),end=" " if (97 <= ord(x.lower()) <= 122 ) else "")



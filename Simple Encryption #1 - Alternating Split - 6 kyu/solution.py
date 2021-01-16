#Take every 2nd char from the string, then the other chars, that are not every 2nd char, and concat them as new String.


def encrypt(text, n):
    
    if text == None:
        encrypted_text = None
    else:
        encrypted_text = ""
        if n >= 1:
            #the algorithm takes the even numbered indexes and place them at the start, then puts the odd at the end
            for i in range(1,(len(text)),2):
                encrypted_text += text[i]
            
            for i in range(0,(len(text)),2):
                encrypted_text += text[i]
            n -= 1
        else:
            encrypted_text = text
    
    return encrypted_text if n < 1 else (encrypt(encrypted_text,n))


def decrypt(encrypted_text,n):
    
    if encrypted_text == None:
        text = None
    else:
        text = ""
        fh = encrypted_text[:int(len(encrypted_text)/2)] 
        sh = encrypted_text[int(len(encrypted_text)/2):]
        #this takes two containers first half(even numbered indexes), second half (odd numbered indexes)
        #and takes the contents and places them in a third container in an alternating fashion
        if n >= 1:
            for i in range(int(len(encrypted_text)/2)):
                text += sh[i]
                text += fh[i]
        #if the string has an odd number of indexes it appends the last item as the last item(which never moves)
            if (len(encrypted_text) % 2) == 1:
                text += sh[-1]
            n -= 1
        else:
            text = encrypted_text
    return text if n < 1 else (decrypt(text,n))
        
    

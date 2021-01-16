def digital_root(n):
    x = 0
    while True:
        for i in str(n):
            x += int(i)
        n = x
        
        if len(str(x)) == 1:
            break
        x = 0
    return x 
    
print(digital_root(169))


#OP one liner
# def digital_root(n):
#     return n if n < 10 else digital_root(sum(map(int,str(n))))

# print(map(int,str(169)))
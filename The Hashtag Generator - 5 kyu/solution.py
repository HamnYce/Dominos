def generate_hashtag(s):
    comp = ""
    for i in s.split():
        comp += i.lower().capitalize()
    return False if (len(comp) > 140 or s == "") else ("#"+comp)
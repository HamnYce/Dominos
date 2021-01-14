import re
def increment_string(strng):
    print(strng)
    if strng == "":
        return "1"
    if not strng[-1].isdigit():
        return strng +"1"
    if strng.isdigit():
        return str(int(strng)+1).zfill(len(strng))
    m = re.match(r".*?([0-9]+)$",strng)
    num = m.group(1)

    n = str(int(num)+1)
    print(m.groups())
    return "".join([strng[:len(strng)-len(num)],str(n).zfill(len(num))])

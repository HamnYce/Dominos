import os
import requests
import sys

LANGS = {
        "py":'py',
        "python":"py",
        "java":"java",
        "c++":"cpp",
        "cpp":"cpp"
        }

arg_list = sys.argv[1:]
if len(arg_list) == 2:
    slug = arg_list[0]
    lang = arg_list[1]
else:
    slug = input("What is the url/slug of the Kata? ")
    lang  = input("Which language will you be using [Python/Java/C++]? ").lower()


# get kata data from codewars API
if ".com" in slug:
    slug = max(slug.split("/"),key=len)
url = f"https://www.codewars.com/api/v1/code-challenges/{slug}"
resp = requests.get(url=url)
data = resp.json()
if 'name' not in data:
    print("Invalid url/slug! please check your input and try again")
    exit()

ext = LANGS.get(lang)
if not ext: 
    print("Invalid language / language not available")
    exit()

# init data
name = data['name'].replace("/","-")
desc = data['description']
kyu = data["rank"]['name']

# sanitize name into valid file name
name = "".join(x for x in name if x.isalnum() or x == " ")

#directory name
dname = f"{name} - {kyu}"

# Create Directory for kata
try:
    os.mkdir(dname)
except Exception as e:
    print(f"Directory not created. Error: {e}")
    exit()

# cd into created directory and generate files
os.chdir(dname)
md = open(f"README.md","w")
md.write(desc)
md.close()
solution = open(f"solution.{ext}","w")
solution.close()
print(f"Directory '{dname}' and files created succesfully!")

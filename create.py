import os
import requests
slug = input("What is the url/slug of the Kata?")
if ".com" in slug:
    slug = max(slug.split("/"),key=len)
url = f"https://www.codewars.com/api/v1/code-challenges/{slug}"
resp = requests.get(url=url)
data = resp.json()
if 'name' not in data:
    print("Invalid url/slug! please check your input and try again")
    exit()
name = data['name'].replace("/","-")
desc = data['description']
kyu = data["rank"]['name']

dname = f"{name} - {kyu}"
try:
    os.mkdir(dname)
except Exception as e:
    print(f"Directory not created. Error: {e}")
    exit()
print(f"Directory '{dname}' created!")
os.chdir(dname)
md = open(f"README.md","w")
md.write(desc)
md.close()
py = open(f"solution.py","w")
py.close()

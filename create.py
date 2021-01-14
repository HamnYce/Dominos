import os
import requests
slug = input("What is the url/slug of the Kata?")
if ".com" in slug:
    slug = slug.split("/")[-1]
url = f"https://www.codewars.com/api/v1/code-challenges/{slug}"

resp = requests.get(url=url)
data = resp.json()
name = data['name']
desc = data['description']
kyu = data["rank"]['name']

dname = f"{name} - {kyu}"
os.mkdir(dname)
print(f"Directory '{dname}' created!")
os.chdir(dname)
md = open(f"{name}.md","w")
md.write(desc)
md.close()
py = open(f"solution.py","w")
py.close()

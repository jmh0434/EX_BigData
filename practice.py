import requests
from bs4 import BeautifulSoup

req = requests.get("https://www.naver.com")
html = req.text
soup = BeautifulSoup(html, "html.parser")

print(soup.title)
print(soup.title.name)
print(soup.title.string)

from email.mime import application, image
from urllib import response
from bs4 import BeautifulSoup
import requests

session=requests.Session()

headers={
    "User-Agent":Mozilla/5.0
    "accept":text/html,application/xhtml+xhtml,application/xml=0.9,
    image/webp,*/*;q=0.8,
    "accept-language":ja,en-us;q=0.8,en;q=0.6
    "content-type"*:application/x-www-form-urlencoded
    "origin"="https://twitter.com",
    "upgrade-insecure-requests":"1"
}

response=session.get("https://twitter.com/",headers=headers,allow_redirects=True)
soup=BeautifulSoup(response.text,"lxml")
auth_token=soup.find(attrs={"name":"autenticity_token"}).get("value")

print("autenticity_token: "+auth_token)
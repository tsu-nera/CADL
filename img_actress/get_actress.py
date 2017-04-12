from os.path  import basename
import urllib.request
import requests
from bs4 import BeautifulSoup
from time import sleep

pages = ['http://www.dmm.co.jp/mono/dvd/-/ranking/=/term=monthly/mode=actress/rank=1_20/', 
         'http://www.dmm.co.jp/mono/dvd/-/ranking/=/term=monthly/mode=actress/rank=21_40/',
         'http://www.dmm.co.jp/mono/dvd/-/ranking/=/term=monthly/mode=actress/rank=41_60/',
         'http://www.dmm.co.jp/mono/dvd/-/ranking/=/term=monthly/mode=actress/rank=61_80/',
         'http://www.dmm.co.jp/mono/dvd/-/ranking/=/term=monthly/mode=actress/rank=81_100/']

for page in pages:
    html = urllib.request.urlopen(page).read()

    soup = BeautifulSoup(html, 'html.parser')

    tables = soup.find_all('table', {'class': 'w100 mg-b20 work'})
    for table in tables:
        for block in table.findAll("td", attrs = {"class": "bd-b"}):
            img = block.find("img")
            link = img['src']
            with open(basename(link), "wb") as f:
                print(link)
                f.write(requests.get(link).content)

#!/usr/bin/env python3
import requests, json, pyprind
from bs4 import BeautifulSoup

def startCrawler(fileName):
    prod_dict={}
    base_url = "http://www.gomaji.com/"
    json_arr = []

    res = requests.get('http://www.gomaji.com/index.php?city=Taichung&tag_id=99')
    soup = BeautifulSoup(res.text)
    # liTag = soup.find_all("li","box-shadow2px ")

    recipNum = len(soup.select('ul.deal16 li.box-shadow2px'))
    ProgreBar = pyprind.ProgBar(recipNum,title = "共 %d 個餐廳要處理" % recipNum)
    #建立一個進度條物件

    for i in soup.select('ul.deal16 li.box-shadow2px'):
        href = i.find('a')['href']# 把a的href屬性的值抓出來
        href = base_url+href

        name = i.find('a').find('div','boxc').find('h2')# find可以找到他的child那一層
        name = name.text.strip()

        d = {name: href}
        json_arr.append(d)
        ProgreBar.update()#item_id可以讓使用者追蹤到底執行到第幾個ID
            #ID通常是放for loop裏面的變數，update()會讓進度條更新

    with open(fileName, 'w', encoding='UTF-8') as f:
        json.dump(json_arr, f)

if __name__  ==  "__main__":
    startCrawler('gomaji.json')
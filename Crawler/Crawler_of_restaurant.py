#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests, json, pyprind, sys
from bs4 import BeautifulSoup

def startCrawler(fileName):
    prod_dict={}
    base_url = "http://www.gomaji.com/"
    json_arr = []

    res = requests.get('http://www.gomaji.com/index.php?city=Taichung&tag_id=99')
    soup = BeautifulSoup(res.text)

    recipNum = len(soup.select('ul.deal16 li.box-shadow2px'))
    ProgreBar = pyprind.ProgBar(recipNum,title = "共 %d 個餐廳要處理" % recipNum)
    #建立一個進度條物件

    for i in soup.select('ul.deal16 li.box-shadow2px'):
        href = i.find('a')['href']# 把a的href屬性的值抓出來
        href = base_url+href

        name = i.find('a').find('div','boxc').find('h2')# find可以找到他的child那一層
        name = name.text.strip()

        d = {"restaurant": name, "url":href}
        json_arr.append(d)
        ProgreBar.update()#item_id可以讓使用者追蹤到底執行到第幾個ID
            #ID通常是放for loop裏面的變數，update()會讓進度條更新

    with open(fileName, 'w', encoding='UTF-8') as f:
        json.dump(json_arr, f)

if __name__  ==  "__main__":
    if len(sys.argv) < 2:
        #sys.argv[0]是模組名稱喔!
        print("Usage:\n\tpython[3] "+sys.argv[0]+" <filename.json>")
        print("\n\tURL can be:http://www.gomaji.com/index.php?city=Taichung&tag_id=99");
        sys.exit(1)#0為正常結束，其他數字exit會拋出一個例外，可以被捕獲
    startCrawler(sys.argv[1])
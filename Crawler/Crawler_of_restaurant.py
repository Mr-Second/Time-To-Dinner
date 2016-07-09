#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests, json, pyprind, sys
from bs4 import BeautifulSoup
base_url = "http://www.gomaji.com/"
json_arr = []

def startCrawler(fileName):
    res = requests.get('http://www.gomaji.com/index.php?city=Taichung')
    #一開始的台中頁面  然後去爬上面所有的餐廳分類網址
    soup = BeautifulSoup(res.text)

    aLen = len(soup.select("#lb_tag  a"))/2 # "lb_tag  a"是餐廳分類的tag 但是每個分類都有2個重複的tag，所以要/2
    aIndex = 1
    recipNum = len(soup.select('ul.deal16 li.box-shadow2px'))
    ProgreBar = pyprind.ProgBar(aLen, title = "共 %d 個餐廳類別要處理" % aLen)
    for a in soup.select("#lb_tag  a"):
        href = a['href']
        if aIndex > aLen: break
        parsePage(base_url+href)
        aIndex = aIndex + 1
        ProgreBar.update(1,item_id = aIndex, force_flush=True)#item_id可以讓使用者追蹤到底執行到第幾個ID
        #ID通常是放for loop裏面的變數，update()會讓進度條更新


    #建立一個進度條物件
    dump(fileName)

def parsePage(url):
    res = requests.get(url)
    childSoup = BeautifulSoup(res.text)

    for i in childSoup.select('ul.deal16 li.box-shadow2px'):
        href = i.find('a')['href']# 把a的href屬性的值抓出來
        href = base_url+href

        name = i.find('a').find('div','boxc').find('h2')# find可以找到他的child那一層
        name = name.text.strip()

        d = {"restaurant": name, "url":href}
        json_arr.append(d)

def dump(fileName):
    with open(fileName, 'w', encoding='UTF-8') as f:
        json.dump(json_arr, f)    

if __name__  ==  "__main__":
    if len(sys.argv) < 2:
        #sys.argv[0]是模組名稱喔!
        print("Usage:\n\tpython[3] "+sys.argv[0]+" <filename.json>")
        print("\n\tURL can be:http://www.gomaji.com/index.php?city=Taichung&tag_id=99");
        sys.exit(1)#0為正常結束，其他數字exit會拋出一個例外，可以被捕獲
    startCrawler(sys.argv[1])
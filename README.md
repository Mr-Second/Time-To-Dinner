# 吃飯小幫手（t2e）[![Build Status](https://travis-ci.org/david30907d/KCM.svg?branch=master)](https://travis-ci.org/david30907d/KCM)

吃飯小幫手的網頁版，使用django佈署，與整個系統共用一個session但是可以獨立佈署的專案

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisities

1. OS：Ubuntu / OSX would be nice
2. environment：need python3 `sudo apt-get update; sudo apt-get install; python3 python3-dev`

### Installing

1. `git clone https://github.com/Stufinite/time2eat.git`
2. `pip install -r requirements.txt`

## Running & Testing

## Run

* Execute : `python manage.py runserver`. If it work fine on [here] , then it's done. Congratulations~~

### Break down into end to end tests

目前還沒寫測試...

### And coding style tests

目前沒有coding style tests...

### Results

API使用方式（下面所寫的是api的URL pattern）：

* 餐廳資料：
  * 取得所有餐廳列表：`/t2e/api/restaurant/list/`
    * result:
      ```
      [
        {
          "ResLike": 50,
          "ResName": "鼎日竹業爭飯",
          "avatar": "/media/%E9%8D%8B%E8%A3%A1%E9%8D%8B%E7%89%A9_gygOC9M.jpg",
          "score": 3
        }
      ]
      ```
  * 取得特定餐廳的詳細介紹：`/t2e/api/restaurant/prof/?res_id=1`
  res_id是餐廳的id，可以把1改成任意阿拉伯數字
    * result:
      ```
      {
        "ResFavorDish": [
          [
            "今日特餐",
            100
          ]
        ],
        "ResLike": 50,
        "ResName": "鼎日竹業爭飯",
        "address": "中興",
        "avatar": "/media/%E9%8D%8B%E8%A3%A1%E9%8D%8B%E7%89%A9_gygOC9M.jpg",
        "country": "臺灣",
        "date": [
          "一",
          "二"
        ],
        "envText": "以新鮮食材佐特製湯頭，搭配風格設計空間，讓聚餐除了享受美食，也能提升時尚品味！",
        "environment": "/media/%E9%9B%9E%E8%BF%B7%E8%BF%AD%E9%A6%99.jpg",
        "feature": "/media/%E6%A9%99%E9%A6%99%E9%AD%9A.jpg",
        "featureText": "均勻分布的油花與鮮紅肉質，讓口感更加紮實不凡，肉獨有的香氣與油花潤飾，放進精心熬煮清甜的湯汁中輕涮，令人流連忘返的香滑柔嫩口感，讓你感動不已！",
        "last_reserv": "20：00",
        "phone": [
          "0972804840",
          "0912356789"
        ],
        "score": 3
      }
      ```
  * 取得特定餐廳的所有餐點：`/t2e/api/restaurant/menu/?res_id=1`
  res_id是餐廳的id，可以把1改成任意阿拉伯數字
    * result:
      ```
      {
        "dish": [
          {
            "image": "/media/images/time2eat/turkey.svg",
            "isSpicy": true,
            "name": "今日特餐",
            "price": 65
          }
        ],
        "menu": [
          "/media/%E9%9B%9E%E8%BF%B7%E8%BF%AD%E9%A6%99_rSrzyjA.jpg"
        ]
      }
      ```
* 訂單資料：
  * 餐廳訂單：
    * 指定日期：`/t2e/api/order/?res_id=1&dateString=2016-10-23`

    (res_id是餐廳的id，可以把1改成任意阿拉伯數字，dateString可以替換成任意日期)
    * 不指定日期（預設會提供當日的資料）：`/t2e/api/order/?res_id=1`

    res_id是餐廳的id，可以把1改成任意阿拉伯數字
    * result:
    ```
    {
      "Date": "2016-10-23",
      "OrderList": [
        {
          "Create": "2016-10-23T06:10:35.924Z",
          "ResOrder": {
            "今日特餐": 2
          },
          "total": 130
        },
        ...
      ],
      "ResAddress": "中興",
      "ResName": "鼎日竹業爭飯",
      "Score": 3,
      "Type": [
        "中式"
      ]
    }
    ```
  * 使用者訂單：
    * 指定日期：`/t2e/api/order/user/?dateString=2016-10-23`

    (dateString可以替換成任意日期)
    * 不指定日期（預設會提供當日的資料）：`/t2e/api/order/user/`
    * result:
    ```
    {
      "Date": "2016-10-23",
      "FDish": "今日特餐",
      "Ftype": "中式",
      "Order": [
        {
          "create": "2016-10-23T06:10:36.052Z",
          "meal": [
            [
              "今日特餐",
              2
            ]
          ],
          "total": 130
        },
        ...
      ],
      "User": "root"
    }
    ```

## Deployment

There is no difference between other Django project

You can deploy it with uwsgi, gunicorn or other choice as you want

`吃飯小幫手` 是一般的django專案，所以他佈署的方式並沒有不同

## Built With

* python3.5
* Django==1.10.0

## Versioning

For the versions available, see the [tags on this repository](https://github.com/david30907d/KCM/releases).

## Contributors

* **張泰瑋** [david](https://github.com/david30907d)
* **柯秉廷**
* **黃川哲**

## License

目前還不清楚能不能open source，所以暫不添加License

## Acknowledgments

[here]: http://127.0.0.1:8000/t2e/all_list
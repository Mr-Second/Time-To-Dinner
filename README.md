# Inferno 地獄  

就只是個中二的名子  
讓我寫程式的時候比較爽  

Inferno 是[七原罪](httpL://github.com/stufinite/journey)的載體，詳細的七原罪架構規劃在這邊 [連結](httpL://github.com/stufinite/journey)  
Inferno會是一個通用的論壇型式框架  
七原罪代表七種不同功能的api  都是django app的型式  
可以透過pip，直接安裝到inferno的django project之中  

目前正在進行的七原罪：

1. 暴食：安裝完成，[察看api](httpL://github.com/stufinite/gluttony)
2. 怠惰：進行中
3. 色欲：進行中

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisities

1. OS：Ubuntu / OSX would be nice
2. environment：need python3 `sudo apt-get update; sudo apt-get install; python3 python3-dev`

### Installing

1. `git clone https://github.com/Stufinite/inferno.git`
2. 使用虛擬環境：
  1. `virtualenv venv`
  2. 啟動方法
    1. for Linux：`. venv/bin/activate`
    2. for Windows：`venv\Scripts\activate`
3. `pip install -r requirements.txt`

## Running & Testing

## Run

1. 下載測試用的[資料庫](https://drive.google.com/open?id=0B19mg1oUrRQ3R0FWN3NEWjNYVzg)進去（裏面有預設好的測資），放到time2eat的資料夾底下，然後把名子改成db.sqlite3（覆蓋舊的資料庫）。
2. Execute : `python manage.py runserver`. If it work fine on [here] , then it's done. Congratulations~~

### Break down into end to end tests

目前還沒寫測試...

### And coding style tests

目前沒有coding style tests...

### Results


## Built With

* python3.5
* Django==1.10.0

## Contributors

* **張泰瑋** [david](https://github.com/david30907d)
* **柯秉廷**
* **黃川哲**
* **鍾孟儒**
* **范霖**
* **松松**

## License

## Acknowledgments

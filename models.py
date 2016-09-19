# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime
# Create your models here.
# 要取得會員的model要這樣寫
from oscar.core.compat import get_user_model
from apps.user.models import User
User = get_user_model()

class Type(models.Model):
    ResType = models.CharField(max_length=10)
    def __str__(self):
        return self.ResType

class ResProf(models.Model):
    ResName = models.CharField(max_length=30, default='') # 餐廳名稱
    address = models.CharField(max_length=30, default='')
    district = models.CharField(max_length=10, default='') # 例如：南區
    ResLike = models.DecimalField(default=50,max_digits=6, decimal_places=0  ) # always add default value!
    score = models.DecimalField(default=3,max_digits=1, decimal_places=0)
    last_reserv = models.CharField(max_length=20)
    ResType = models.ManyToManyField(Type) # 餐廳的料理類型
    country = models.CharField(max_length=10) # 哪個國家的餐廳
    def __str__(self):
      return self.ResName

class Date(models.Model):
    # Date 是用來存星期幾有開店
    DayOfWeek = models.CharField(max_length=1) # 表示星期幾
    Start = models.CharField(max_length=8) # 開始營業時間
    CloseMid = models.CharField(max_length=8, default='') # 中午結束營業時間（店家中午不一定休息，所以允許空字串）
    StartMid = models.CharField(max_length=8, default='') # 下午重新開始營業時間（店家中午不一定休息，所以允許空字串）
    Close = models.CharField(max_length=8) # 結束營業時間
    restaurant = models.ForeignKey(ResProf) # 有開店的日子，一對多的關係
    def __str__(self):
        return self.DayOfWeek + self.Start + '~' + self.Close

class Phone(models.Model):
    phoneNum = models.CharField(max_length=15) # 電話號碼
    restaurant = models.ForeignKey(ResProf) # 考慮到一間店可能有多隻聯絡電話
    def __str__(self):
        return self.phoneNum

class Dish(models.Model):
    DishName = models.CharField(max_length=20) # 菜名
    price = models.DecimalField(max_digits=6, decimal_places=0) # 價錢
    isSpicy = models.BooleanField()
    restaurant = models.ForeignKey(ResProf) # 餐廳的餐點
    def __str__(self):
        return self.DishName

class Order(models.Model):
    # 餐廳的訂單，是一個一對多的關係，因為一間餐廳會有多張訂單
    restaurant = models.ForeignKey(ResProf)
    create = models.DateTimeField() # 訂單的精確時間
    date = models.CharField(max_length=10) # 訂單的年月日
    period = models.CharField(max_length=3) # 標示是早中午哪個時段
    total = models.DecimalField(max_digits=8, decimal_places=0) # 該訂單總額
    def __str__(self):
        return self.date + ' ' + str(self.restaurant)

class SmallOrder(models.Model):
    # 以同一道菜去彙整的訂單子集合
    dish = models.OneToOneField(Dish)
    orderUser = models.ManyToManyField(User) # 為了要紀錄使用者有定過哪些菜色（這邊很有問題）
    amount = models.DecimalField(max_digits=5, decimal_places=0) # 訂購該餐點的數量
    order = models.ForeignKey(Order) # 隸屬的訂單
    def __str__(self):
        return str(self.dish) + ' ' + str(self.amount) + '份'

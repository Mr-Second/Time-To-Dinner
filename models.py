# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime
# Create your models here.
class Type(models.Model):
    country = models.CharField(max_length=10)
    ResType = models.CharField(max_length=10)
    def __str__(self):
        return self.ResType

class ResProf(models.Model):
    restaurant = models.CharField(max_length=30, default='')
    address = models.CharField(max_length=30, default='')
    district = models.CharField(max_length=10, default='')
    service_h = models.CharField(max_length=50, default='')
    phone = models.CharField(max_length=12, default='')
    ResLike = models.DecimalField(default=50,max_digits=6, decimal_places=0  )#always add default value!
    score = models.DecimalField(default=3,max_digits=1, decimal_places=0)
    last_reserv = models.CharField(max_length=20)
    ResType = models.ManyToManyField(Type)
    create = models.DateTimeField()
    def __str__(self):
      return self.restaurant
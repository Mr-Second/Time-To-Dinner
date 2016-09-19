from django.contrib import admin
from apps.time2eat.models import Type, ResProf, Date, Phone, Dish, Order, SmallOrder
# Register your models here.
admin.site.register(Type)
admin.site.register(ResProf)
admin.site.register(Date)
admin.site.register(Phone)
admin.site.register(Dish)
admin.site.register(Order)
admin.site.register(SmallOrder)
class ResProf(admin.ModelAdmin):
    list_display = ('ResName', 'ResType', 'score')
    search_fields = ('ResName',)

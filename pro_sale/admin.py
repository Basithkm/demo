from django.contrib import admin
from . models import *
from . import models

# Register your models here.

# admin.site.register(SellCategory)
# admin.site.register(SellProperty)
# admin.site.register(SaleMessages)

@admin.register(models.SaleMessages)
class SaleMessagesAdmin(admin.ModelAdmin):
    list_display =['id','user','full_name','phone','sale_property','intrest','date_and_time']

# admin.site.register(Image)

@admin.register(models.SellProperty)
class SellPropertyAdmin(admin.ModelAdmin):
    list_display =['id','rent_title','user','you_are','rent_property_category','approved','upload_date']
    list_filter =['id','rent_property_category','district','upload_date']
    search_fields =['user__email','rent_property_category__rent_property_category','rent_title','district__district_name','city__city_name']



@admin.register(models.SaleMultipleImages)
class SellImagesAdmin(admin.ModelAdmin):
    list_display =['id','user','sell_property_id','sell_property','images']

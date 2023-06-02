from django.contrib import admin
from . models import *


from . import models

# Register your models here.




admin.site.register(District)
admin.site.register(City)
admin.site.register(RentType)
admin.site.register(RentPropertyCategory)
admin.site.register(YouAre)
admin.site.register(RentTypeCategory)
admin.site.register(BasedSize)
# admin.site.register(RentProperty)



@admin.register(models.RentMultipleImages)
class RentImagesAdmin(admin.ModelAdmin):
    list_display =['id','user','rent_property_id','rent_property','images']


@admin.register(models.RentMessages)
class RentMessagesAdmin(admin.ModelAdmin):
    list_display =['id','user','full_name','phone','sale_property','intrest','date_and_time']
    
# @admin.register(models.RentProperty)

@admin.register(models.RentProperty)
class RentPropertyAdmin(admin.ModelAdmin):
    
    list_display =['id','rent_title','user','you_are','rent_type','rent_property_category','approved','upload_date']
    # list_editable = ['rent_price']
    list_filter =['id','rent_type','rent_property_category','district','upload_date']
    # ordering =['rent_type','rent_property_category','rent_title','district','city']
    list_per_page = 10
    search_fields =['user__email','rent_type__rent_type_name','rent_property_category__rent_property_category','rent_title','district__district_name','city__city_name']




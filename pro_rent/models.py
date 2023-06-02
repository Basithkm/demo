from django.db import models
from django.core.validators import MinValueValidator
from registration.models import Account
# from django.contrib.postgres.fields import ArrayField
# from pro_sale.models import SellProperty
# Create your models here.
from PIL import Image
from ckeditor.fields import RichTextField


class BasedSize(models.Model):
    per_size = models.CharField(max_length=255,blank=True,null=True)


    def __str__(self) -> str:
        return self.per_size



class District(models.Model):
    # id = models.IntegerField(primary_key=True) 
    district_name =models.CharField(max_length=100,blank=True,null=True)

    def __str__(self) -> str:
        return self.district_name

class City(models.Model):
    district =models.ForeignKey(District,on_delete=models.CASCADE,blank=True,null=True)
    city_name =models.CharField(max_length=255,blank=True,null=True)
    def __str__(self) -> str:
        return self.city_name
    
class RentType(models.Model):
    rent_type_name =models.CharField(max_length=100,blank=True,null=True)

    def __str__(self) -> str:
        return self.rent_type_name
    

class YouAre(models.Model):
    you_are =models.CharField(max_length=100,null=False,blank=False)
    def __str__(self) -> str:
        return self.you_are


class RentPropertyCategory(models.Model):
    rent_property_category =models.CharField(max_length=100,null=True,blank=True)

    def __str__(self) -> str:
        return self.rent_property_category
    

class RentTypeCategory(models.Model):
    rent_property_category =models.ForeignKey(RentPropertyCategory,on_delete=models.CASCADE,max_length=100,null=False,blank=False)
    reny_type_category = models.CharField(max_length=100,null=False,blank=False)

    def __str__(self) -> str:
        return self.reny_type_category
        
    
class RentProperty(models.Model):
    user = models.ForeignKey(Account,on_delete=models.CASCADE)
    rent_property_category =models.ForeignKey (RentPropertyCategory,on_delete=models.CASCADE,blank=False,null=False)
    reny_type_category =models.ForeignKey(RentTypeCategory,on_delete=models.CASCADE,null=True,blank=True)
    rent_title =models.CharField(max_length=255,blank=True,null=True)
    property_name=models.CharField(max_length=100,null=True,blank=False)
    you_are=models.ForeignKey(YouAre,on_delete=models.CASCADE,blank=True,null=True)
    agent_name =models.CharField(max_length=100,null=True,blank=True)
    agent_company =models.CharField(max_length=100,null=True,blank=True)
    rent_type =models.ForeignKey(RentType,on_delete=models.CASCADE,blank=True,null=True)
    daily_rent=models.FloatField(blank=True,null=True)
    monthly_rent =models.FloatField(blank=True,null=True)
    lease_rent = models.FloatField(blank=True,null=True)
    number_of_persons = models.IntegerField(blank=True,null=True)
    number_of_beds = models.IntegerField(blank=True,null=True)
    num_of_rooms =models.IntegerField(blank=True,null=True,validators=[MinValueValidator(1)])
    num_of_bathrooms =models.IntegerField(blank=True,null=True,validators=[MinValueValidator(1)])
    balcony=models.CharField(max_length=100,null=True,blank=True)
    furnished=models.CharField(max_length=100,null=True,blank=True)
    admin_area=models.CharField(max_length=100,null=True,blank=True)
    confrence_room=models.CharField(max_length=100,null=True,blank=True)
    type_of_soil=models.CharField(max_length=100,null=True,blank=True)
    extras =models.TextField(blank=True,null=True)
    rent_image=models.ImageField(upload_to='rent_images/',blank=True,null=True,editable=True,help_text="sale images",verbose_name="sale images")
    rent_size_in_squrefeet =models.IntegerField(blank=True,null=True)
    property_acre =models.FloatField(blank=True,null=True)
    per_size =models.ForeignKey(BasedSize,on_delete=models.CASCADE,blank=True,null=True)
    rent_price =models.IntegerField(blank=True,null=True,validators=[MinValueValidator(1)])
    rent_description =RichTextField(blank=True,null=True)
    district =models.ForeignKey(District,on_delete=models.CASCADE,blank=False,null=False)
    city = models.ForeignKey(City,on_delete=models.CASCADE,blank=False,null=False)
    approved = models.BooleanField(default=False)
    upload_date =models.DateField(auto_now_add=True)


    def __str__(self):
        return self.rent_title
    
    class Meta:
        ordering =['rent_title']



    def save(self):
        if self.rent_image:          
            super(RentProperty, self).save()
            rent_image = Image.open(self.rent_image)
            (width , height) = rent_image.size     
            size = (720,480)
            image = rent_image.resize(size, Image.ANTIALIAS)
            image.save(self.rent_image.path)
        else:
            if self.rent_property_category:  
                super(RentProperty, self).save()


class RentMultipleImages(models.Model):
    user = models.ForeignKey(Account,on_delete=models.CASCADE)
    rent_property = models.ForeignKey(RentProperty, on_delete=models.CASCADE, related_name='image')
    images = models.ImageField(upload_to='proprty_images')

    def __str__(self):
        return f"Image for {self.rent_property.property_name}"
  
class RentMessages(models.Model):
    user =models.ForeignKey(Account,on_delete=models.CASCADE)
    sale_property =models.ForeignKey(RentProperty,on_delete=models.CASCADE)
    full_name =models.CharField(null=True,blank=True,max_length=255)
    phone =models.CharField(max_length=20,null=True,blank=True)
    email =models.EmailField(null=True,blank=True)
    intrest =models.CharField(max_length=255,null=True,blank=True)
    date_and_time = models.DateTimeField(auto_now_add=True)

  


   

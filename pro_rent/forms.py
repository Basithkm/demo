# from django import forms
# from . models import City,RentProperty




# class RentPropertyForm(forms.ModelForm):
#     class Meta:
#         model = RentProperty
#         fields = ('rent_type','rent_property_category','title','image','size','price','description','state','city')


#         def __init__(self,*args, **kwargs):
#             super().__init__(*args, **kwargs)
#             self.fields['city'].queryset =City.objects.none()
#             if 'state' in self.data:
#                 try:
#                     state_id =int(self.data.get('state'))
#                     self.fields['city'].queryset=City.objects.filter(state_id=state_id).order_by('title')
#                 except(ValueError,TypeError):
#                     pass

#             elif self.instance.pk:
#                 self.fields['city'].queryset =self.instance.state.city_set.order_by()
from django.urls import path
from . import views

urlpatterns = [
    path('property-sale',views.property_for_sale,name="property_for_sale"),
    path('my_sale_properies/<int:id>',views.get_my_sale_properies,name="my_sale_properies"),
    path('post-free-add-property-for-sale',views.post_free_add_property_for_sale,name="post_free_add_property_for_sale"),


    path('get_sale_property/<int:id>',views.get_sale_property,name='get_sale_property'),
    path('delete_your_sale_property/<int:id>',views.delete_your_sale_property,name='delete_your_sale_property'),

    path('sale_residenteial_purpose/<int:pk>/',views.sale_residenteial_purpose, name='sale_residenteial_purpose'), 
    path('sale_commertial_purpose/<int:pk>/', views.sale_commertial_purpose, name='sale_commertial_purpose'),
    path('sale_land_view/<int:pk>/', views.sale_land_view, name='sale_land_view'),
    path('sale_you_are_form/<int:pk>/', views.sale_you_are_form, name='sale_you_are_form'),
    path('saleyouare/<int:pk>/', views.sale_you_are, name='sale_you_are'), 


    # path('update_sale_product/<int:id>',views.update_sale_property,name='update_sale_property'),

    # path('update_sale_product/<int:id>',views.update_sale_product,name='update_product'),
    # path('youare/<int:pk>/', views.you_are, name='you_are'), 
    # path('you_are_form/<int:pk>/', views.you_are_form, name='you_are_form'),

    # path('search/', views.search, name='search'),

    path('salesearch/',views.salesearch, name='salesearch'),
    path('saleautocomplete/',views.saleautocomplete, name='saleautocomplete'),
    path('locatesaleautocomplete/',views.locate_sale_autocomplete, name='locatesaleautocomplete'),


    path('salefilter/', views.sale_product_filter, name='sale_product_filter'),


    

]






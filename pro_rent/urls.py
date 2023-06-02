from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('property-for-rent',views.property_for_rent,name="property_for_rent"),
    # path('search_for_sale',views.search_for_sale,name="search_for_sale"),
    path('my_rent_properies/<int:id>',views.my_rent_properies,name="my_rent_properies"),

    path('get_cities/', views.get_cities, name='get_cities'), 
    path('get_types/', views.get_types, name='get_types'), 


    path('residenteial_purpose/<int:pk>/', views.residenteial_purpose, name='residenteial_purpose'), 
    path('youare/<int:pk>/', views.you_are, name='you_are'), 
    path('you_are_form/<int:pk>/', views.you_are_form, name='you_are_form'),


    path('get_rent_property/<int:id>',views.get_rent_property,name='get_rent_property'),


    path('rent_type/<int:pk>/', views.rent_type, name='rent_type'),
    path('daily_rent/<int:pk>/', views.daily_rent, name='daily_rent'),
    path('monthly_rent/<int:pk>/', views.monthly_rent, name='monthly_rent'),
    path('lease_rent/<int:pk>/', views.lease_rent, name='lease_rent'),
    path('flatmate/<int:pk>/', views.flatmate, name='flatmate'),



    # path('update_your_rent_property/<int:pk>',views.update_your_rent_property,name='update_your_rent_property'),

    path('commertial_purpose/<int:pk>/', views.commertial_purpose, name='commertial_purpose'),
    path('land_view/<int:pk>/', views.land_view, name='land_view'),



    path('post-free-add-property-for-rent',views.post_free_add_property_for_rent,name="post_free_add_property_for_rent"),
    path('delete_property/<int:id>',views.delete_your_rent_property,name='delete_your_rent_property'),



    path('search/', views.search, name='search'),
    # path('autocomplete/', views.autocomplete, name='autocomplete'),

    path('spaceautocomplete/', views.spaceautocomplete, name='spaceautocomplete'),
    # path('salespaceautocomplete/', views.salespaceautocomplete, name='salespaceautocomplete'),
    

    # path('salespaceautocomplete/', views.salespaceautocomplete, name='salespaceautocomplete'),
    path('locaterentautocomplete/',views.locate_rent_autocomplete, name='locaterentautocomplete'),
    path('locatesaleautocomplete/',views.locate_sale_autocomplete, name='locatesaleautocomplete'),


    path('categoryrentautocomplete/',views.category_rent_autocomplete, name='categoryrentautocomplete'),
    path('categorysaleautocomplete/',views.category_sale_autocomplete, name='categorysaleautocomplete'),


    path('filter/',views.product_filter,name='product_filter'),


]

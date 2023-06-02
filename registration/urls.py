from . import views
from django.urls import path

# app_name= 'account'

urlpatterns = [
    # path('', views.home, name='home'),
    path('add-post/',views.add_post,name="add_post"),
    path('get-my-account',views.get_my_account,name="get_my_account"),
    path('register/', views.register, name='register'),
    path('activate/<uidb64>/<token>/', views.activate_email , name='activate'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
 
    

]
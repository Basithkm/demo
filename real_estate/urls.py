"""real_estate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from pro_rent import views



admin.site. site_header ='Real Estate Admin'
admin. site. index_title = 'Admin Panel'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('pro_rent.urls')),
    path('sale/',include('pro_sale.urls'),name="pro_sale"),
    path('account/', include('registration.urls')),
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('allauth.socialaccount.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

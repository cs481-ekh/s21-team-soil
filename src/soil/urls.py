"""soil URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, re_path, include
from soil.soil_samples import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('report/', views.get_report),
    path('authenticate/', views.authenticate_user),
    path('userlist/', views.get_users),
    #re_path(r'^api/soil/insert_soil_sample/$', views.insert_soil_sample),
    path('user_tracking/', include('user_tracking.urls')),
]

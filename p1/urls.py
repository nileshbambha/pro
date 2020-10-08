from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('register',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('input/',views.input,name='input'),
    path('logout/',views.logout,name='logout'),
    path('',views.index,name='index'),
    path('<int:data_id>',views.details,name='details'),
    path('<int:datas_id>/',views.deletes,name='deletes'),
]

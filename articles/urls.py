

from django.contrib import admin
from django.urls import path, include
from . import views


app_name= "articles"
urlpatterns = [
    path('',views.article, name ="articles"),
    path('création_article/', views.créer, name= "créer"),
    path('<slug:slug>/', views.contenus, name = "contenus_article")
   
]

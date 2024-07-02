from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('login', views.login),
    path('loginUser', views.check_credentials),
    path('homepage', views.go_to_homepage),	   
]

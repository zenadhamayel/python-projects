from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('gratenum', views.randNum),
    path('clear',views.clearsessions),
]
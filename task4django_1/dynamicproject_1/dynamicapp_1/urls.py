from django.urls import path
from dynamicapp_1 import views

urlpatterns = [

    path('', views.fun1, name="fun1"),
    path('news/', views.fun2, name="fun2"),
    path('contact/', views.fun3, name="fun3"),
    path('destinations/', views.fun4, name="fun4"),
    path('elements/', views.fun5, name="fun5"),
]

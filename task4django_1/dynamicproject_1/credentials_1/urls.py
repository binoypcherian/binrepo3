from django.urls import path
from credentials_1 import views

urlpatterns = [
    path('register/',views.fun6,name="fun6"),
    path('login/',views.fun7,name="fun7"),
    path('logout/',views.fun8,name="fun8"),
    ]
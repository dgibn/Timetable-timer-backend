from django.urls import path

from . import views

urlpatterns= [
    path("",views.day,name="day"),
    path("",views.week,name="week"),
    path("",views.month,name="month")
]
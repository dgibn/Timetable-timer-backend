from django.urls import path
from . import views

urlpatterns= [
    path("day/",views.day,name="day"),
    path("week/",views.week,name="week"),
    path("month/",views.month,name="month"),
]

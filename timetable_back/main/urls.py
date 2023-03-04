from django.urls import path
from . import views
from main import views

urlpatterns= [
    path("day/",views.day,name="day"),
    path("week/",views.week,name="week"),
    path("month/",views.month,name="month"),
    path("add",views.add, name="add"),
    path("update/<event_id>/",views.update, name="update"),
    path("delete/<event_id>/",views.delete, name="delete"),
    path("event_info/<int:pk>",views.Event_detail, name="event_detail") ,
    
    path("event_info/",views.Event_detail_all, name="event_detail_all"),
    
    

    
    
]

from django.urls import path
from . import views
from main import views

urlpatterns= [
    
    path("add_event",views.add_Event, name="add"),
    path("update_event/<int:pk>",views.update_event, name="update"),
    path("event_info/<int:pk>/delete/", views.delete_event, name='delete'),
    path("event_info/<int:pk>",views.Event_detail, name="event_detail") ,
    path("event_info/",views.Event_detail_all, name="event_detail_all"),
        
]

from django.shortcuts import render,redirect
from main.models import Event
from .serializers import timetable_serializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.generics import get_object_or_404


 
# Create your views here.


@api_view(['GET'])
def Event_detail(request,pk):               #get detail of a particular event
    event = Event.objects.get(id=pk)
    serializer = timetable_serializer(event)
    return Response(serializer.data)

@api_view(['GET'])
def Event_detail_all(request):              #get detail of all events
        event = Event.objects.all()
        serializer = timetable_serializer(event,many=True)
        return Response(serializer.data)

@api_view(['POST'])
def add_Event(request):                     #add a new event(input in json format)
    serializer = timetable_serializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response()

@api_view(['PUT'])
def update_event(request,pk):          #update an event
    try:
        instance = Event.objects.get(pk=pk)
    except Event.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        
    serializer = timetable_serializer(instance, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    

@api_view(['DELETE'])                       #delete an event
def delete_event(self,pk):
    event = Event.objects.get(id=pk)
    event.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    



     
     







    

    


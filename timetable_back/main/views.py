from django.shortcuts import render,redirect
from main.models import Event
from main.forms import Eventreg
from .serializers import timetable_serializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view


 




# Create your views here.

def day(request):
    day_events = Event.objects.all
    return render(request, 'day.html', { 'day' : day_events })

def week(request):
    return render(request, 'week.html', {})

def month(request):
    return render(request, 'month.html', {})

def add(request):

    if request.method =="POST":
        form = Eventreg(request.POST or None)
        if form.is_valid():
            form.save()
        print("data saved")
        return redirect('add')

    else:
        return render(request, 'add.html', {})
    
def update(request, event_id):
    
    update_event = Event.objects.get(pk=event_id)
    form = Eventreg(request.POST or None, instance=update_event)
    if form.is_valid():
        form.save()
        return redirect('day')

    return render(request, 'update.html', 
                  { 'uevent' : update_event, 'form' : form})

def delete(request, event_id):
    delete_event = Event.objects.get(pk=event_id)
    delete_event.delete()
    return redirect('day')

@api_view(['GET'])
def Event_detail(request,pk):
    event = Event.objects.get(id=pk)
    serializer = timetable_serializer(event)
    return Response(serializer.data)

@api_view(['GET'])
def Event_detail_all(request):
        event = Event.objects.all()
        serializer = timetable_serializer(event,many=True)
        return Response(serializer.data)







    

    


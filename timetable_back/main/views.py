from django.shortcuts import render,redirect
from main.models import Event
from main.forms import Eventreg


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
        return redirect('day')

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
    

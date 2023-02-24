from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def day(resonse):
    return HttpResponse("<h1>Calender day view</h1>")

def week(resonse):
    return HttpResponse("<h1>Calender week view</h1>")

def month(resonse):
    return HttpResponse("<h1>Calender month view</h1>")

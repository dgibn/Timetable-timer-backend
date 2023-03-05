from django import forms
from main.models import Event

class Eventreg(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'desc', 'stime', 'etime', 'done']

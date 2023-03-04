from rest_framework import serializers
from main.models import Event

class timetable_serializer(serializers.Serializer):
    class Meta:
        model = Event
        fields = ('id', 'name', 'desc', 'stime', 'etime', 'done')
        read_only_fields = ('id',)

    name = serializers.CharField(max_length=200)
    desc = serializers.CharField(max_length=500, default="Description")
    stime = serializers.DateTimeField
    etime = serializers.DateTimeField
    done = serializers.BooleanField


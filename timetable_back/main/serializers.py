from rest_framework import serializers

class timetable_serializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    desc = serializers.CharField(max_length=500, default="Description")
    stime = serializers.DateTimeField
    etime = serializers.DateTimeField
    done = serializers.BooleanField


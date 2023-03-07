from rest_framework import serializers
from main.models import Event

class timetable_serializer(serializers.Serializer):
    class Meta:
        model = Event
        fields = ('id', 'name', 'desc', 'stime', 'etime', 'done')
        read_only_fields = ('id',)

    name = serializers.CharField(max_length=200)
    desc = serializers.CharField(max_length=500, default="Description")
    stime = serializers.DateTimeField()
    etime = serializers.DateTimeField()
    done = serializers.BooleanField()


    def create(self, validated_data):
        return Event.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.desc = validated_data.get('desc', instance.desc)
        instance.stime = validated_data.get('stime', instance.stime)
        instance.etime = validated_data.get('etime', instance.etime)
        instance.done = validated_data.get('done', instance.done)
        instance.save()
        return instance


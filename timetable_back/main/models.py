from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=500, default="Description")
    stime = models.DateTimeField(null=True)
    etime = models.DateTimeField(null=True)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.name

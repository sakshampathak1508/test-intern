from django.db import models
from django.utils import timezone


class Restaurant(models.Model):
    name = models.CharField(max_length=256,default="")
    res_type = models.CharField(max_length=256,default="")
    desc = models.TextField(blank=True)
    day =  models.CharField(max_length=10,default="")
    open_time =  models.TimeField(default=timezone.now)
    close_time = models.TimeField(default=timezone.now)
    is_closed = models.BooleanField(default=False)
    

    def __str__(self):
        return self.name +' '+self.day
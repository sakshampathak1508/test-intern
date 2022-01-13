from django.db import models
from django.utils import timezone
# Create your models here.
class Hour(models.Model):
    day =  models.CharField(max_length=10,default="")
    open_time =  models.DateTimeField(default=timezone.now)
    close_time = models.DateTimeField(default=timezone.now)
    is_closed = models.BooleanField(default=False)


class Restaurant(models.Model):
    name = models.CharField(max_length=256,default="")
    res_type = models.CharField(max_length=256,default="")
    desc = models.TextField(blank=True)
    hours = models.ForeignKey('menu.Hour',on_delete=models.CASCADE) 
    

    def __str__(self):
        return self.name
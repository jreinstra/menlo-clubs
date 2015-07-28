from django.db import models

# Create your models here.
class Club(models.Model):
    name = models.CharField(max_length=50)
    short_description = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    
    meeting_day = models.CharField(max_length=9)
    meeting_time = models.TimeField()
    
    def __str__(self):
        return self.name
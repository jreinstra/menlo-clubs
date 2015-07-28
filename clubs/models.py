from django.db import models

# Create your models here.
class Club(models.Model):
    name = models.CharField(max_length=50)
    short_description = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    
    meeting_day = models.CharField(max_length=9)
    meeting_time = models.TimeField()
    meeting_location = models.CharField(max_length=50)
    
    contact_email = models.CharField(max_length=200)
    
    def meeting_time_string(self):
        return self.meeting_day + "s at " + self.meeting_time.strftime("%H:%M %p").lower()
    
    def __str__(self):
        return self.name
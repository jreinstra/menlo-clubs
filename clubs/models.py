from django.db import models

# Create your models here.
class Club(models.Model):
    MON = "Monday"
    TUE = "Tuesday"
    WED = "Wednesday"
    THU = "Thursday"
    FRI = "Friday"
    SAT = "Saturday"
    SUN = "Sunday"
    MEETING_DAYS = (
        (0, MON),
        (1, TUE),
        (2, WED),
        (3, THU),
        (4, FRI),
        (5, SAT),
        (6, SUN)
    )
    
    name = models.CharField(max_length=50)
    short_description = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    
    meeting_day = models.IntegerField(max_length=9, choices=MEETING_DAYS, default=(0, MON))
    meeting_time = models.TimeField()
    meeting_location = models.CharField(max_length=50)
    
    contact_email = models.CharField(max_length=200)
    
    def meeting_time_string(self):
        return self.meeting_day + "s at " + self.meeting_time.strftime("%H:%M %p").lower()
    
    def __str__(self):
        return self.name
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
    NON = "Non Weekly"
    MEETING_DAYS = (
        (0, MON),
        (1, TUE),
        (2, WED),
        (3, THU),
        (4, FRI),
        (5, SAT),
        (6, SUN),
        (7, NON),
    )
    MEETING_DAYS_LIST = (MON, TUE, WED, THU, FRI, SAT, SUN)
    
    name = models.CharField(max_length=50)
    short_description = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    
    meeting_day = models.IntegerField(choices=MEETING_DAYS, default=0)
    meeting_time = models.TimeField()
    meeting_location = models.CharField(max_length=50)
    
    student_leaders = models.CharField(max_length=200, default="")
    teacher_leaders = models.CharField(max_length=200, default="")
    contact_email = models.CharField(max_length=200, default="")
    
    meets_biweekly = models.BooleanField(default=False)
    meets_monthly = models.BooleanField(default=False)
    meets_irregularly = models.BooleanField(default=False)
    
    def meeting_time_string(self):
        try:
            result = self.MEETING_DAYS_LIST[self.meeting_day] + "s at "
        except IndexError:
            result = ""
        
        return result + self.meeting_time.strftime("%H:%M %p").lower()
    
    def __str__(self):
        return self.name
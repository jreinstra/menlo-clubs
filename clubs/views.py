from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import DetailView

from .models import Club

import json

# Create your views here.
def index(request):
    return redirect("clubs:club_list")

def club_list(request):
    days = [x[0] for x in Club.MEETING_DAYS]
    clubs_by_day = {}
    for day in days:
        clubs_by_day[day] = Club.objects.filter(meeting_day=day)
    return render(request, 'clubs/club_list.html', {'clubs_by_day':clubs_by_day})
    
class ClubDetail(DetailView):
    model = Club
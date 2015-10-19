from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import DetailView

from .models import Club

import json

# Create your views here.
def index(request):
    return redirect("clubs:club_list")

def club_list(request):
    if request.META['HTTP_HOST'] == "salty-beyond-2520.herokuapp.com":
        return HttpResponseRedirect("http://menloclubs.org/")
    days = Club.MEETING_DAYS
    clubs_by_day = []
    for day_id, day in days:
        clubs = list(Club.objects.filter(meeting_day=day_id))
        if len(clubs) > 0:
            clubs_by_day.append((day, clubs))
        else:
            clubs_by_day.append((day, None))
    #return HttpResponse(clubs_by_day["Tuesday"])
    return render(request, 'clubs/club_list.html', {'clubs_by_day':clubs_by_day})
    
class ClubDetail(DetailView):
    model = Club
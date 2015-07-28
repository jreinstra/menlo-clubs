from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView

from .models import Club

# Create your views here.
def index(request):
    return redirect("clubs:club_list")

class ClubList(ListView):
    model = Club
    
    
class ClubDetail(DetailView):
    model = Club
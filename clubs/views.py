from django.shortcuts import render
from django.http import HttpResponse

from .models import Club

# Create your views here.
def index(request):
    return render(request, 'clubs/clubs.html', {'clubs':Club.objects.all()})
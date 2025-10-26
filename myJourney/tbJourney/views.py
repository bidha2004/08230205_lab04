from django.shortcuts import render
from .models import Profile, LearningJourney

def index(request):
    journey = LearningJourney.objects.first()
    return render(request, 'index.html', {'journey': journey})

def aboutMe(request):
    profile = Profile.objects.first()
    return render(request, 'aboutMe.html', {'profile': profile})

from django.shortcuts import render
from .models import Profile

# Create your views here.

def profiles(request):
    profiles = Profile.objects.all()
    return render(request, 'profiles.html', context={'profiles': profiles})

def profile(request):
    return render(request, 'profile.html')

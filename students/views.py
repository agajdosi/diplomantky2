from django.shortcuts import render

from .models import Profile

# Create your views here.

def profiles(request):
    profiles = Profile.objects.all()
    return render(request, 'profiles.html', context={'profiles': profiles})

def profile(request, first_name, last_name):
    profile = Profile.objects.get(
        user__first_name__iexact = first_name,
        user__last_name__iexact = last_name
        )
    return render(request, 'profile.html', context={'profile': profile})

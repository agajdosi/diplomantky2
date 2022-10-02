from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import Profile
from .forms import ProfileForm

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

def profile_edit(request, first_name, last_name):
    profile = Profile.objects.get(
        user__first_name__iexact = first_name,
        user__last_name__iexact = last_name
        )

    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile.portfolio = form.cleaned_data['portfolio']
            profile.save()
            return HttpResponseRedirect('/')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'profile_edit.html', context={'profileform': form})

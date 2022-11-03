from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .models import Profile
from .forms import ProfileForm


def profiles(request):
    profiles = Profile.objects.all()
    return render(request, 'profiles.html', context={'profiles': profiles})


def show_portfolio(request, first_name, last_name):
    """Show the portfolio page of the artist by first name and last name."""
    profile = Profile.objects.get(
        user__first_name__iexact = first_name,
        user__last_name__iexact = last_name
        )

    return render(request, 'portfolio.html', context={'profile': profile})


@login_required(login_url='/admin/login/')
def edit_portfolio(request, first_name, last_name):
    """Edit the portfolio. Available only for the user who is owner of portfolio."""
    path = request.path[:-1].rpartition('/')
    profile = Profile.objects.get(
        user__first_name__iexact = first_name,
        user__last_name__iexact = last_name
        )

    if profile.user != request.user:
      return HttpResponseRedirect(f'{path[0]}/')
    
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if not form.is_valid():
            return render(request, 'edit_portfolio..html', context={'profileform': form})
        profile.portfolio = form.cleaned_data['portfolio']
        profile.save()
        return HttpResponseRedirect(f'{path[0]}/')

    form = ProfileForm(instance=profile)
    return render(request, 'edit_portfolio.html', context={'profileform': form})

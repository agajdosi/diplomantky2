from django.urls import path

from .views import profile, profiles, profile_edit

urlpatterns = [
  path('', profiles),
  path('<str:first_name>-<str:last_name>/', profile),
  path('<str:first_name>-<str:last_name>/edit', profile_edit),
]
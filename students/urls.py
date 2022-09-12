from django.urls import path

from .views import profile, profiles

urlpatterns = [
  path('', profiles),
  path('<str:first_name>-<str:last_name>/', profile),
]
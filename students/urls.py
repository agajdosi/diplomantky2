from django.urls import path

from .views import profiles, show_portfolio, edit_portfolio


urlpatterns = [
  path('', profiles),
  path('<str:first_name>-<str:last_name>/', show_portfolio),
  path('<str:first_name>-<str:last_name>/edit/', edit_portfolio),
]
from django.urls import path

from .views import index, graduates, show_portfolio, edit_portfolio, exhibitions


urlpatterns = [
  path('', index),
  path('graduates', graduates),
  path('exhibitions', exhibitions),
  path('<str:first_name>-<str:last_name>/', show_portfolio),
  path('<str:first_name>-<str:last_name>/edit/', edit_portfolio),
]
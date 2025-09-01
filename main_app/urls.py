from django.urls import path, include 
from django.contrib import admin
from .models import Console
from . import views
# these are the actual urls. the name is a reference that takes us to that url we just made.
urlpatterns = [
      path('consoles/list/', views.all_consoles, name='console_list'),
      path('consoles/<int:pk>/details/', views.console_details, name='console_details'),
      path('consoles/create/', views.console_create, name='create'),
      path('consoles/<int:pk>/edit', views.ConsoleUpdateView.as_view(), name='console_update')
]

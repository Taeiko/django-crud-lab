from django.shortcuts import render, redirect
from .models import Console
# Create your views here.
def all_consoles(request):
    consoles = Console.objects.all()
    return render (request, 'consoles/console-list.html',{'consoles': consoles})

from django.shortcuts import render, redirect
from .models import Console
# Create your views here.
# these are basically the pages we request our site to show us when we type the link.
def all_consoles(request):
    consoles = Console.objects.all()
    return render (request, 'game-consoles/console_list.html',{'consoles': consoles})

def console_details(request, pk):
    console = Console.objects.get(pk=pk)
    return render(request, 'game-consoles/console_details.html',{'console':console} )
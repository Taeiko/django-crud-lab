from django.shortcuts import render, redirect
from .models import Console
from .forms import ConsoleForm
# from forms import ConsoleForm
# Create your views here.
# these are basically the pages we request our site to show us when we type the link.
def all_consoles(request):
    consoles = Console.objects.all()
    return render (request, 'game-consoles/console_list.html',{'consoles': consoles})

def console_details(request):
    console = Console.objects.get()
    return render(request, 'game-consoles/console_details.html',{'console':console} )


def console_create(request):
    if request.method=="POST":
        form = ConsoleForm(request.POST)
        if form.is_valid():
            console = form.save
        return redirect('conosole_details', pk=console.pk)
    else:
        form = ConsoleForm()
    return render (request, 'game-consoles/console_form.html',{"form" : form})
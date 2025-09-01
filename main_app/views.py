from django.shortcuts import render, redirect
from .models import Console
from .forms import ConsoleForm
# from forms import ConsoleForm
# Create your views here.
# these are basically the pages we request our site to show us when we type the link.
def all_consoles(request):
    consoles = Console.objects.all()
    return render (request, 'game-consoles/console_list.html',{'consoles': consoles})

def console_details(request, pk):
    console = Console.objects.get(pk=pk)
    return render(request, 'game-consoles/console_details.html',{'console':console} )


def console_create(request):
    if request.method=="POST":
        form = ConsoleForm(request.POST)
        if form.is_valid():
            console = form.save()
        return redirect('console_details', pk=console.pk)
    else:
        form = ConsoleForm()
    return render (request, 'game-consoles/console_form.html',{"form" : form})


from django.urls import reverse_lazy, reverse 
from django.views.generic import UpdateView, DeleteView
from django.views import View
from .models import Console
from .forms import ConsoleForm


class ConsoleUpdateView(UpdateView):
    model = Console 
    form_class = ConsoleForm
    template_name = 'game-consoles/console_form.html'
    
    def get_success_url(self):
        return reverse ('console_details', kwargs={'pk':self.object.pk})



class CosnoleDeleteView(DeleteView):
    model = Console
    template_name = 'game-consoles/console_confirm_delete.html'
    success_url = reverse_lazy("console_list")
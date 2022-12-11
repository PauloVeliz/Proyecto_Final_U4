from django.shortcuts import render,redirect
from django.views.generic.list import ListView
from .models import Proyecto
from django.contrib import messages
from .forms import RegisterForm,ProyectoForm

# Create your views here.

# Vista basada en clase

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request,f'Usuario {username} creado.')
            return redirect('login')
    else:
        form = RegisterForm()
    
    context = {'form':form}
    return render(request,'register.html',context)


class ProyectoView(ListView):
    model = Proyecto
    template_name = 'portafolio.html'
    context_object_name="proyectos"


def post(request):
    context = {}
    context['form']= ProyectoForm()

    if request.method == "POST":
        form = ProyectoForm(request.POST)
        if form.is_valid():
            titulo_proyecto = form.cleaned_data['titulo_proyecto']
            messages.success(request,f'Proyecto {titulo_proyecto} creado.')
            form.save()
            return redirect('portafolio')
    else:
        form = ProyectoForm()
    
    context = {'form':form}
    
    return render(request, "form.html", context)

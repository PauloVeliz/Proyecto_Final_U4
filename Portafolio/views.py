from django.shortcuts import render,redirect
from django.views.generic.list import ListView
from .models import Proyecto,Guardar_IP
from django.contrib import messages
from .forms import RegisterForm,ProyectoForm
from ipware import get_client_ip

# Create your views here.


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
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ip,is_routable = get_client_ip(self.request)
        ip_guardada = Guardar_IP.objects.filter(IP=ip).first()
        if ip_guardada is None:
            form = Guardar_IP(IP=ip)
            form.save()
        return context


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

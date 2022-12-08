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
            return redirect('proyecto')
    else:
        form = RegisterForm()
    
    context = {'form':form}
    return render(request,'register.html',context)


class ProyectoView(ListView):
    model = Proyecto
    template_name = 'portafolio.html'

def post(request):
    context = {}
    context['form']= ProyectoForm()

    if request.method == "POST":
        form = ProyectoForm(request.POST)
        if form.is_valid():
            titulo_proyecto = form.cleaned_data['titulo_proyecto']
            messages.success(request,f'Proyecto {titulo_proyecto} creado.')
            form.save()
            return redirect('proyecto')
    else:
        form = ProyectoForm()
    
    context = {'form':form}
    
    return render(request, "form.html", context)



# # Vista basada en clase
# class proyecto(ListView):
#     def post():
#         titulo = form.clean_data['titulo']
#         tags = form.clean_data['tags']


#         proyecto = Proyecto(titulo,)
#         Proyecto.save()

#         redirect('portafolio')
#         # Para ver toda la info que se ha creado


# # Vista basada en función

# def ListBook(request):
#     list_book = Book.objects.all()
#     paginator = Paginator(list_book,10)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     return render(request, 'booklist.html', {'page_obj': page_obj})
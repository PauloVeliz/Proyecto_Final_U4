from django.urls import path
from .views import ProyectoView
from . import views
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('portafolio/',login_required(ProyectoView.as_view()),name='portafolio'),
    path('register/',views.register,name='register'),
    path('login/',LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/',LogoutView.as_view(template_name='logout.html'),name='logout'),
    path('post/',login_required(views.post),name='post'),

]
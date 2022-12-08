from django.urls import path
from .views import ProyectoView
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('',ProyectoView.as_view(),name='proyecto'),
    path('register/',views.register,name='register'),
    path('login/',LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/',LogoutView.as_view(template_name='logout.html'),name='logout'),
    path('post/',views.post,name='post')

]
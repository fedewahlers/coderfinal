from django.shortcuts import render, redirect
from .models import Autor, Editorial, Libro
from .forms import AutorForm, EditorialForm, LibroForm
from django.contrib.auth import views as auth_views
from django.urls import path
from django.views.generic import TemplateView
from .models import Blog
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.shortcuts import render




def crear_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crear_autor')
    else:
        form = AutorForm()
    return render(request, 'crear_autor.html', {'form': form})

def crear_editorial(request):
    if request.method == 'POST':
        form = EditorialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crear_editorial')
    else:
        form = EditorialForm()
    return render(request, 'crear_editorial.html', {'form': form})

def crear_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crear_libro')
    else:
        form = LibroForm()
    return render(request, 'crear_libro.html', {'form': form})

def buscar_libro(request):
    query = request.GET.get('q')
    libros = Libro.objects.filter(titulo__icontains=query) if query else Libro.objects.all()
    return render(request, 'buscar_libro.html', {'libros': libros})


def home(request):
  if request.user.is_authenticated:
    return render(request, 'home.html')
  else:
       form = AuthenticationForm()
       return render(request, 'home.html', {'form': form})
       
class HomeView(TemplateView):
    template_name = 'home.html'
    

from django.shortcuts import render

def about(request):
    return render(request, 'about.html')

def blog_list(request):
    blogs = Blog.objects.all()  # Asegúrate de que tienes un modelo Blog
    return render(request, 'blog_list.html', {'blogs': blogs})

from django.shortcuts import get_object_or_404

def blog_detail(request, page_id):
    blog = get_object_or_404(Blog, id=page_id)  # Asegúrate de que tienes un modelo Blog
    return render(request, 'blog_detail.html', {'blog': blog})
def mi_vista_protegida(request):
    # Lógica de la vista
    return render(request, 'mi_plantilla.html')
def vista_para_admin(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden("No tienes permisos para acceder a esta página.")

urlpatterns = [
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    # Otras URLs...
]

def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    else:
        messages.warning(request, "Debes iniciar sesión para acceder a esta página.")
        return redirect('login')
    
    

from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm

@login_required
def profile_update(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirige a una página de perfil o donde desees
    else:
        form = ProfileUpdateForm(instance=request.user.profile)
    return render(request, 'profile_update.html', {'form': form})



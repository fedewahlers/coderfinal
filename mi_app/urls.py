from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import HomeView
from django.urls import path
from . import views
from django.conf.urls.static import static



urlpatterns = [
    path('crear_autor/', views.crear_autor, name='crear_autor'),
    path('crear_editorial/', views.crear_editorial, name='crear_editorial'),
    path('crear_libro/', views.crear_libro, name='crear_libro'),
    path('buscar_libro/', views.buscar_libro, name='buscar_libro'),
   path('', views.home, name='home'),path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('pages/', views.blog_list, name='blog_list'),
    path('pages/<int:page_id>/', views.blog_detail, name='blog_detail'),
       path('', HomeView.as_view(), name='home'),  # Página de inicio
           path('', views.home, name='home'),
           
           path('profile/update/', views.profile_update, name='profile_update'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
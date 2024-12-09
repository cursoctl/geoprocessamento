
from django.contrib import admin
from django.urls import path, include
from mapa import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # Adicionando URL para a página inicial
    path('mapa/', include('mapa.urls')),  # Incluindo URLs do app mapa
]

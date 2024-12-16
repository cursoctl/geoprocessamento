
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from mapa import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # Adicionando URL para a página inicial
    path('mapa/', include('mapa.urls')),  # Incluindo URLs do app mapa
]

# Configuração para servir arquivos de mídia no modo de desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

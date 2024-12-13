from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


# URLs principais 
main_patterns = [
    path('', views.index, name='index'),  # Página inicial
    path('galeria/', views.galeria, name='galeria'),  # Galeria de imagens
    path('contato/', views.contato, name='contato'),  # Página de contato
    path('servicos/', views.servicos, name='servicos'),  # Lista de serviços
]

# URLs de funcionalidades relacionadas a mapas
mapa_patterns = [
    path('mapa/', views.mapa_view, name='mapa'),  # Visualização de mapa
    path('criar/mapa/', views.criar_mapa, name='criar_mapa'),  # Criar novo mapa
    path('mapa/upload/', views.mapa_upload, name='mapa_upload'),  # Upload de mapa
]

# Combinação de todas as URLs
urlpatterns = main_patterns + mapa_patterns

# Adiciona URLs para arquivos de mídia apenas se estiver no modo de desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


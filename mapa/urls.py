from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mapa/', views.mapa_view, name='mapa'),
    path('galeria/', views.galeria, name='galeria'),
    path('contato/', views.contato, name='contato'),
    path('servicos/', views.servicos, name='servicos'),
    path('criar/mapa/', views.criar_mapa, name='criar_mapa'),
    path('mapa/upload/', views.mapa_upload, name='mapa_upload'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

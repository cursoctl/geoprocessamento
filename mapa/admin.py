from django.contrib import admin
from django.utils.html import format_html
from .models import Mapa, Imagem, Servico,Projeto
from django.db import models

class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('titulo','descricao','link')
    search_fields = ('titulo',)
class ImagemAdmin(admin.ModelAdmin):

    nome = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='imagens/')

    # Função para exibir a miniatura da imagem no admin
    def get_imagem_thumbnail(self, obj):
        if obj.imagem:
            return format_html('<img src="{}" width="50" height="50" />', obj.imagem.url)
        return 'No image'
    get_imagem_thumbnail.short_description = 'Thumbnail'

    # Função para exibir a URL da imagem
    def get_imagem_url(self, obj):
        return obj.imagem.url if obj.imagem else 'No image'
    get_imagem_url.short_description = 'Imagem URL'

admin.site.register(Imagem, ImagemAdmin)
admin.site.register(Projeto, ProjetoAdmin)

@admin.register(Mapa)
class MapaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'imagem')
    search_fields = ('nome', 'descricao')


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')
    search_fields = ('nome', 'descricao')



import folium
from django.shortcuts import render, redirect
from .models import Mapa, Imagem, Servico
from .forms import ContatoForm, MapaForm
from django.contrib import messages

def criar_mapa(request):
    if request.method == 'POST':
        form = MapaForm(request.POST, request.FILES)  # O `request.FILES` é necessário para upload de arquivos
        if form.is_valid():
            form.save()
            messages.success(request, 'Mapa criado com sucesso!')
            return redirect('index')  # Redireciona para a página inicial ou outra página
    else:
        form = MapaForm()

    return render(request, 'criar_mapa.html', {'form': form})

def mapa_view(request):
    mapa_obj = folium.Map(location=[-23.5505, -46.6333], zoom_start=12)
    pois = Mapa.objects.all()  # Obtém todos os objetos Mapa
    for ponto in pois:
        if hasattr(ponto, 'localizacao') and ponto.localizacao:
            folium.Marker(
                [ponto.localizacao.y, ponto.localizacao.x], 
                popup=ponto.nome
            ).add_to(mapa_obj)

    # Converte o mapa para HTML
    mapa_html = mapa_obj._repr_html_()
    return render(request, 'mapa.html', {'mapa': mapa_html})

def index(request):
    imagens = Imagem.objects.all()[:4]  # Obtém as primeiras 4 imagens
    return render(request, 'index.html', {'imagens': imagens})


def galeria(request):
    imagens = Imagem.objects.all()  # Obtém todas as imagens
    return render(request, 'galeria.html', {'imagens': imagens})

def contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.send_email()  # Envia o email (implementar no form)
            messages.success(request, 'Mensagem enviada com sucesso!')
            return redirect('contato')
    else:
        form = ContatoForm()
    return render(request, 'contato.html', {'form': form})

def servicos(request):
    servicos = Servico.objects.all()
    return render(request, 'servicos.html', {'servicos': servicos})

def mapa_upload(request):
    if request.method == 'POST':
        form = MapaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mapa enviado com sucesso!')
            return redirect('mapa_list')  # Redireciona para uma lista de mapas ou outra página
    else:
        form = MapaForm()
    return render(request, 'mapa/upload.html', {'form': form})

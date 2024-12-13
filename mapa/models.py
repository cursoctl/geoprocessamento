from django.db import models


class Projeto(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='imagens/')
    link = models.URLField(blank=True)

    def __str__(self):
        return self.titulo

class Mapa(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='mapas/', null=True, blank=True)

    def __str__(self):
        return self.nome

class Imagem(models.Model):
    photo = models.ImageField(upload_to='imagens/',blank=True,null=True)
    def __str__(self):
        return str(self.imagem.name)  # Corrigido para acessar corretamente o campo 'imagem'

class Servico(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

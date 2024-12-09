from django import forms
from .models import Mapa
class ContatoForm(forms.Form):
    nome = forms.CharField(max_length=255)
    email = forms.EmailField()
    mensagem = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        # Aqui você pode definir a lógica para enviar o email
        # Por exemplo, utilizando o Django's EmailMessage
        pass
class MapaForm(forms.ModelForm):
    class Meta:
        model = Mapa
        fields = ['nome', 'descricao', 'imagem']
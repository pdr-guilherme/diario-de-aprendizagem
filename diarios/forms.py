from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Entrada, Topico


class TopicoForm(forms.ModelForm):
    class Meta:
        model = Topico
        fields = ["topico"]
        labels = {"topico": "Tópico"}
        widgets = {
            "topico": forms.TextInput(
                attrs={
                    "placeholder": "Insira seu novo tópico aqui",
                    "class": "form-control",
                }
            )
        }


class EntradaForm(forms.ModelForm):
    class Meta:
        model = Entrada
        fields = ["titulo", "texto"]
        labels = {"titulo": "Título", "texto": ""}
        widgets = {
            "titulo": forms.TextInput(
                attrs={
                    "placeholder": "Digite um título que resuma o aprendizado",
                    "class": "form-control",
                }
            ),
            "texto": forms.Textarea(
                attrs={
                    "placeholder": "Digite o que você aprendeu aqui",
                    "class": "form-control",
                }
            ),
        }


class CriarUsuarioForm(UserCreationForm):
    password1 = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Insira sua senha",
                "class": "form-control",
            }
        ),
    )
    password2 = forms.CharField(
        label="Confirmação de Senha",
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Insira sua senha novamente",
                "class": "form-control",
            }
        ),
    )

    class Meta:
        model = User
        fields = ["username"]
        widgets = {
            "username": forms.TextInput(
                attrs={
                    "placeholder": "Digite seu nome de usuário",
                    "class": "form-control",
                }
            ),
        }

"""
URL configuration for diario_aprendizagem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path

from diarios.views import (
    CriarUsuarioView,
    EntradaCreateView,
    EntradaDeleteView,
    EntradaDetailView,
    EntradaListView,
    EntradaUpdateView,
    IndexView,
    LoginViewCustom,
    LogoutViewCustom,
    TopicoCreateView,
    TopicoDeleteView,
    TopicoListView,
)

urlpatterns = [
    path("login/", LoginViewCustom.as_view(), name="login"),
    path("criar-conta/", CriarUsuarioView.as_view(), name="criar_conta"),
    path("logout/", LogoutViewCustom.as_view(), name="logout"),
    path("admin/", admin.site.urls),
    path("", IndexView.as_view(), name="index"),
    path("topicos/", TopicoListView.as_view(), name="topicos"),
    path(
        "<slug:slug_topico>/entradas/",
        EntradaListView.as_view(),
        name="entradas",
    ),
    path(
        "topicos/adicionar/",
        TopicoCreateView.as_view(),
        name="novo_topico",
    ),
    path(
        "topicos/<slug:slug_topico>/apagar/",
        TopicoDeleteView.as_view(),
        name="apagar_topico",
    ),
    path(
        "<slug:slug_topico>/adicionar/",
        EntradaCreateView.as_view(),
        name="nova_entrada",
    ),
    path(
        "<slug:slug_topico>/ver/<str:id>/",
        EntradaDetailView.as_view(),
        name="ver_entrada",
    ),
    path(
        "<slug:slug_topico>/editar/<str:id>/",
        EntradaUpdateView.as_view(),
        name="editar_entrada",
    ),
    path(
        "<slug:slug_topico>/apagar/<str:id>/",
        EntradaDeleteView.as_view(),
        name="apagar_entrada",
    ),
]

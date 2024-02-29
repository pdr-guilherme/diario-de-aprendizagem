from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views import View
from django.views.generic import FormView, TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from .forms import CriarUsuarioForm, EntradaForm, TopicoForm
from .models import Entrada, Topico

# Create your views here.


class LoginViewCustom(LoginView):
    template_name = "diarios/login.html"
    redirect_authenticated_user = True
    fields = "__all__"
    success_url = reverse_lazy("index")


class CriarUsuarioView(FormView):
    template_name = "diarios/criar_conta.html"
    form_class = CriarUsuarioForm
    redirect_authenticated_user = True
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        usuario = form.save()
        if usuario is not None:
            login(self.request, usuario)
        return super(CriarUsuarioView, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return reverse_lazy("topicos")
        return super(CriarUsuarioView, self).get(*args, **kwargs)


class LogoutViewCustom(View):
    def get(self, request):
        logout(request)
        return redirect("index")


class IndexView(TemplateView):
    template_name = "diarios/index.html"


class TopicoListView(LoginRequiredMixin, ListView):
    model = Topico
    template_name = "diarios/topicos.html"
    context_object_name = "topicos"

    def get_queryset(self):
        dono = self.request.user
        topicos = Topico.objects.filter(dono=dono).order_by("topico")
        return topicos


class TopicoCreateView(LoginRequiredMixin, CreateView):
    model = Topico
    form_class = TopicoForm
    template_name = "diarios/novo_topico.html"
    success_url = reverse_lazy("topicos")

    def form_valid(self, form):
        dono = self.request.user
        topicos = Topico.objects.filter(dono=dono)

        for topico in topicos:
            if slugify(form.instance.topico) == topico.slug:
                self.msg_erro = "Já existe um tópico com esse nome!"
                return self.form_invalid(form)

        form.instance.dono = self.request.user
        return super(CreateView, self).form_valid(form)

    def form_invalid(self, form):
        resposta = super().form_invalid(form)
        messages.error(self.request, self.msg_erro)
        return resposta


class TopicoDeleteView(LoginRequiredMixin, DeleteView):
    model = Topico
    template_name = "diarios/apagar_topico.html"
    context_object_name = "topico"
    success_url = reverse_lazy("topicos")

    def get_object(self):
        slug_topico = self.kwargs["slug_topico"]
        dono = self.request.user
        topico = Topico.objects.get(slug=slug_topico, dono=dono)
        return topico


class EntradaListView(LoginRequiredMixin, ListView):
    model = Entrada
    template_name = "diarios/entradas.html"
    context_object_name = "entradas"

    def get_queryset(self):
        slug_topico = self.kwargs["slug_topico"]
        dono = self.request.user
        topico = Topico.objects.get(slug=slug_topico, dono=dono)
        entradas = Entrada.objects.filter(topico=topico).order_by(
            "-adicionada_em"
        )
        return entradas

    def get_context_data(self, **kwargs):
        slug_topico = self.kwargs["slug_topico"]
        dono = self.request.user
        context = super().get_context_data(**kwargs)
        context["topico"] = Topico.objects.get(slug=slug_topico, dono=dono)
        return context


class EntradaCreateView(LoginRequiredMixin, CreateView):
    model = Entrada
    form_class = EntradaForm
    template_name = "diarios/nova_entrada.html"

    def get_context_data(self, **kwargs):
        slug_topico = self.kwargs["slug_topico"]
        dono = self.request.user
        context = super().get_context_data(**kwargs)
        context["topico"] = Topico.objects.get(slug=slug_topico, dono=dono)
        return context

    def get_success_url(self):
        slug_topico = self.kwargs["slug_topico"]
        dono = self.request.user
        topico = Topico.objects.get(slug=slug_topico, dono=dono)
        return reverse_lazy("entradas", kwargs={"slug_topico": topico.slug})

    def form_valid(self, form):
        slug_topico = self.kwargs["slug_topico"]
        dono = self.request.user
        topico = Topico.objects.get(slug=slug_topico, dono=dono)
        form.instance.topico = topico
        return super().form_valid(form)


class EntradaDetailView(LoginRequiredMixin, DetailView):
    model = Entrada
    template_name = "diarios/entrada.html"
    context_object_name = "entrada"

    def get_object(self):
        slug_topico = self.kwargs["slug_topico"]
        dono = self.request.user
        id_entrada = self.kwargs["id"]
        topico = Topico.objects.get(slug=slug_topico, dono=dono)
        obj = Entrada.objects.get(id=id_entrada, topico=topico)
        return obj


class EntradaUpdateView(LoginRequiredMixin, UpdateView):
    model = Entrada
    form_class = EntradaForm
    template_name = "diarios/editar_entrada.html"
    context_object_name = "entrada"

    def get_object(self):
        slug_topico = self.kwargs["slug_topico"]
        dono = self.request.user
        id_entrada = self.kwargs["id"]
        topico = Topico.objects.get(slug=slug_topico, dono=dono)
        obj = Entrada.objects.get(id=id_entrada, topico=topico)
        return obj

    def get_context_data(self, **kwargs):
        slug_topico = self.kwargs["slug_topico"]
        dono = self.request.user
        context = super().get_context_data(**kwargs)
        context["topico"] = Topico.objects.get(slug=slug_topico, dono=dono)
        return context


class EntradaDeleteView(LoginRequiredMixin, DeleteView):
    model = Entrada
    template_name = "diarios/apagar_entrada.html"
    context_object_name = "entrada"

    def get_object(self):
        slug_topico = self.kwargs["slug_topico"]
        dono = self.request.user
        id_entrada = self.kwargs["id"]
        topico = Topico.objects.get(slug=slug_topico, dono=dono)
        obj = Entrada.objects.get(id=id_entrada, topico=topico)
        return obj

    def get_success_url(self):
        slug_topico = self.kwargs["slug_topico"]
        dono = self.request.user
        topico = Topico.objects.get(slug=slug_topico, dono=dono)
        return reverse_lazy("entradas", kwargs={"slug_topico": topico.slug})

    def get_context_data(self, **kwargs):
        slug_topico = self.kwargs["slug_topico"]
        dono = self.request.user
        context = super().get_context_data(**kwargs)
        context["topico"] = Topico.objects.get(slug=slug_topico, dono=dono)
        return context

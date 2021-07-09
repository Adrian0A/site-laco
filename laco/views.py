from typing import ClassVar
import laco
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from laco.models import Laco, Preco, Tema
# Create your views here.


class LacoListView(LoginRequiredMixin, ListView):
    model= Laco
    template_name = 'laco/laco_list.html'

class LacoCreateView(LoginRequiredMixin, CreateView):
    model= Laco
    template_name = 'laco/laco_create.html'

class LacoUpdateView(LoginRequiredMixin, UpdateView):
    model= Laco
    template_name = 'laco/laco_.html'

class LacoDeleteView(LoginRequiredMixin, DeleteView):
    model= Laco

class LacoDetailView(LoginRequiredMixin, DetailView):
    model= Laco


class TemaListView(LoginRequiredMixin, ListView):
    model= Tema

class TemaCreateView(LoginRequiredMixin, CreateView):
    model= Tema

class  TemaDeleteView(LoginRequiredMixin, DeleteView):
    model= Tema


class PrecoListView(LoginRequiredMixin, ListView):
    model= Preco

class PrecoCreateView(LoginRequiredMixin, CreateView):
    model=  Preco

class PrecoUpdateView(LoginRequiredMixin, UpdateView):
    model= Preco

class PrecoDeleteView(LoginRequiredMixin, DeleteView):
    model= Preco

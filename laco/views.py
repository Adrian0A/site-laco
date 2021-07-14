from typing import ClassVar
import laco
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from laco.models import Laco, Preco, Tema


class LacoListView(LoginRequiredMixin, ListView):
    model= Laco
    template_name = 'laco/laco_list.html'

    def get(self,request):
        lc = Laco.objects.all()
        
        ctx = {'laco_list': lc}
        return render(request, self.template_name, ctx)

class LacoCreateView(LoginRequiredMixin, CreateView):
    model= Laco
    fields= ['preco', 'tema', 'descricao']

class LacoUpdateView(LoginRequiredMixin, UpdateView):
    model= Laco

class LacoDeleteView(LoginRequiredMixin, DeleteView):
    model= Laco

class LacoDetailView(LoginRequiredMixin, DetailView):
    model= Laco




class TemaListView(LoginRequiredMixin, ListView):
    model= Tema

class TemaCreateView(LoginRequiredMixin, CreateView):
    model= Tema
    fields = '__all__'

class  TemaDeleteView(LoginRequiredMixin, DeleteView):
    model= Tema




class PrecoListView(LoginRequiredMixin, ListView):
    model= Preco

class PrecoCreateView(LoginRequiredMixin, CreateView):
    model=  Preco
    fields= '__all__'

class PrecoUpdateView(LoginRequiredMixin, UpdateView):
    model= Preco

class PrecoDeleteView(LoginRequiredMixin, DeleteView):
    model= Preco

from laco.form import CreateForm
from django.shortcuts import redirect, render, HttpResponse, get_object_or_404
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
    template_name = 'laco/laco_form.html'
    #fields= ['preco', 'tema', 'descricao', 'picture']
    success_url =  reverse_lazy('laco:all')

    def get(self, request, pk=None):
        form = CreateForm
        ctx = {'form': form}
        return render(request, self.template_name, ctx)

    def post(self, request, pk=None):
        form = CreateForm(request.POST, request.FILES)

        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template_name, ctx)


        form.save()
        return redirect(self.success_url)

class LacoUpdateView(LoginRequiredMixin, UpdateView):
    model= Laco
    fields= ['preco', 'tema', 'descricao', 'picture']
    success_url =  reverse_lazy('laco:all')

class LacoDeleteView(LoginRequiredMixin, DeleteView):
    model= Laco
    success_url =  reverse_lazy('laco:all')

class LacoDetailView(LoginRequiredMixin, DetailView):
    model= Laco

def stream_file(request, pk):
    laco = get_object_or_404(Laco, id=pk)
    response = HttpResponse()
    response['Content-Type'] = laco.content_type
    response['Content-Length'] = len(laco.picture)
    response.write(laco.picture)

    return response




class TemaListView(LoginRequiredMixin, ListView):
    model= Tema
    template_name = 'laco/tema_list.html'

    def get(self,request):
        tm = Tema.objects.all()
        
        ctx = {'tema_list': tm}
        return render(request, self.template_name, ctx)
    

class TemaCreateView(LoginRequiredMixin, CreateView):
    model= Tema
    fields = '__all__'
    success_url= reverse_lazy('laco:tema_list')

class  TemaDeleteView(LoginRequiredMixin, DeleteView):
    model= Tema
    success_url= reverse_lazy('laco:tema_list')




class PrecoListView(LoginRequiredMixin, ListView):
    model= Preco
    template_name = 'laco/preco_list.html'

    def get(self,request):
        pc = Preco.objects.all()
        
        ctx = {'preco_list': pc}
        return render(request, self.template_name, ctx)

class PrecoCreateView(LoginRequiredMixin, CreateView):
    model=  Preco
    fields= '__all__'
    success_url = reverse_lazy('laco:preco_list')

class PrecoUpdateView(LoginRequiredMixin, UpdateView):
    model= Preco
    fields= '__all__'
    success_url = reverse_lazy('laco:preco_list')

class PrecoDeleteView(LoginRequiredMixin, DeleteView):
    model= Preco
    success_url = reverse_lazy('laco:preco_list')

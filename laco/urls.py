from django.urls import path
from . import views

app_name = 'laco'

urlpatterns = [
    path('',views.LacoListView.as_view(), name='all'),

    path('laco/create', views.LacoCreateView.as_view(success_url = 'laco:all'), name='laco_create'),

    path('laco/<int:pk>/update', views.LacoUpdateView.as_view(success_url= 'laco:all'), name='laco_update'),

    path('laco/<int:pk>/delete', views.LacoDeleteView.as_view(success_url= 'laco:all'), name='laco_delete'),

    path('laco/<int:pk>/detail', views.LacoDetailView.as_view(), name='laco_detail'),
    

    path('laco/tema', views.TemaListView.as_view(), name='tema_list'),

    path('laco/tema/create', views.TemaCreateView.as_view(success_url= 'laco:all'), name = 'tema_create'),

    path('laco/tema/<int:pk>/delete', views.TemaDeleteView.as_view(success_url= 'laco:tema_list'), name='tema_delete'),


    path('laco/preco', views.PrecoListView.as_view(), name = 'preco_list'),

    path('laco/preco/create', views.PrecoCreateView.as_view(success_url = 'laco:preco_list'), name = 'preco_create'),

    path('laco/preco/<int:pk>/update', views.PrecoUpdateView.as_view(success_url = 'laco:preco_list'), name = 'preco_update'),
    
    path('laco/preco/<int:pk>/delete', views.PrecoDeleteView.as_view(success_url = 'laco:preco_list'), name = 'preco_delete')
]
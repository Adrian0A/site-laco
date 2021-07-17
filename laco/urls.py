from django.urls import path, reverse_lazy
from . import views

app_name = 'laco'

urlpatterns = [
    path('',views.LacoListView.as_view(), name='all'),

    path('laco/create', views.LacoCreateView.as_view(), name='laco_create'),

    path('laco/<int:pk>/update', views.LacoUpdateView.as_view(), name='laco_update'),

    path('laco/<int:pk>/delete', views.LacoDeleteView.as_view(), name='laco_delete'),

    path('laco/<int:pk>/detail', views.LacoDetailView.as_view(), name='laco_detail'),

    path('laco/<int:pk>/', views.stream_file, name='laco_picture'),
    

    path('laco/tema', views.TemaListView.as_view(), name='tema_list'),

    path('laco/tema/create', views.TemaCreateView.as_view(), name = 'tema_create'),

    path('laco/tema/<int:pk>/delete', views.TemaDeleteView.as_view(), name='tema_delete'),


    path('laco/preco', views.PrecoListView.as_view(), name = 'preco_list'),

    path('laco/preco/create', views.PrecoCreateView.as_view(), name = 'preco_create'),

    path('laco/preco/<int:pk>/update', views.PrecoUpdateView.as_view(), name = 'preco_update'),
    
    path('laco/preco/<int:pk>/delete', views.PrecoDeleteView.as_view(), name = 'preco_delete')
]
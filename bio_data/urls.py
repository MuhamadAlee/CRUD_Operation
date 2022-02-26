from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='data_index'),
    path('create', views.create_new, name='data_create'),
    path('view/<int:data_id>', views.view, name='data_view'),
    path('edit/<int:data_id>', views.edit, name='data_edit'),
    path('delete/<int:data_id>', views.delete, name='data_delete'),
]
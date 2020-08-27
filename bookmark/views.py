from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from .models import Bookmark


# Create your views here.

class BookmarkListView(ListView):
    model = Bookmark
    paginate_by = 6

class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name', 'url']
    success_url = reverse_lazy('list')
    template_name_suffix = '_create'

class BookmarkDetailView(DetailView):
    model = Bookmark

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    #와... field는 못찾네.. _update로 연결이 안된게 아니라 연결이 됐는데 fields가 없으니 표시를 안해주는거였네?
    #without 'fields' 에러 뜨네..
    template_name_suffix = '_update'
    
class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse

from . import models


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'injectme': 'Welcome to the Wiki Demo'})
        return context


class WikiPageListView(ListView):
    model = models.WikiPage
    context_object_name = 'wiki_page_list'
    template_name = "wiki/wiki_page_list.html"


class WikiPageDetailView(DetailView):
    model = models.WikiPage
    context_object_name = 'wiki_page_detail'
    template_name = "wiki/wiki_page_detail.html"


class WikiPageCreateView(CreateView):
    model = models.WikiPage
    template_name = "wiki/wiki_page_form.html"
    fields = ('title', 'text')


class WikiPageUpdateView(UpdateView):
    model = models.WikiPage
    template_name = "wiki/wiki_page_form.html"
    fields = ('title', 'text')


class WikiPageDeleteView(DeleteView):
    context_object_name = 'wiki_page'
    model = models.WikiPage
    template_name = "wiki/wiki_page_confirm_delete.html"
    success_url = reverse_lazy('wiki:list')

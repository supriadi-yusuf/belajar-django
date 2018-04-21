from django.shortcuts import render
from django.views.generic import ListView, DetailView

from publishing.models import Publisher

# Create your views here.

class PublishingListView(ListView):
    model = Publisher

class PublishingDetailView(DetailView):
    model = Publisher

    def get_context_data(self, **kwargs):
        context = super(PublishingDetailView, self).get_context_data(**kwargs)
        context['pesan'] = 'Halo kawan semua'
        return context

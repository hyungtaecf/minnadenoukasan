from django.shortcuts import render
from django.views.generic import TemplateView

class StoreView(TemplateView):
    template_name = 'store/index.html'

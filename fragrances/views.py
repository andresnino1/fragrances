from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from .models import FragrancesModel


# Create your views here.

# esta es la vista que retorna al home
class HomePageView(TemplateView):
    template_name = 'home.html'


# esta es la vista que retorna al dashboard
class DashBoardView(TemplateView):
    template_name = 'dashboard.html'


# esta vista retorna la LISTA de fragramcias al dashboard
class FragrancesList(ListView):
    model = FragrancesModel
    template_name = 'dashboard.html'
    context_object_name = 'fragrance_list'

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView
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
    context_object_name = 'fragrance_list'  # esta categoria renombra objetc_list por un nombre mas legible
    paginate_by = 2


# esta vista retorna la pagina de detalle de cada Fragrancia

class FragrancesDetailView(DetailView):
    model = FragrancesModel
    context_object_name = 'fragrance_detail'
    template_name = 'fragrances-detail.html'

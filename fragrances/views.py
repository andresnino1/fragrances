from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView
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
    paginate_by = 3



# esta vista retorna la pagina de detalle de cada Fragrancia

class FragrancesDetailView(DetailView):
    model = FragrancesModel
    context_object_name = 'fragrance_detail'
    template_name = 'fragrances-detail.html'


# this view is a form to add new fragrances in database

class AddFragrancesView(CreateView):
    model = FragrancesModel
    context_object_name = 'create_fragrance'
    fields = '__all__'
    template_name = "addfragrance.html"
    #success_url = reverse_lazy('dashboard')
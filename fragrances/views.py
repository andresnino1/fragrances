from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from .models import FragrancesModel
from .filters import FragranceFilter


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

# In this section I am adding the filter as a context and it passes to the template
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['fragrance_filter'] = FragranceFilter(self.request.GET, queryset=self.get_queryset() )
        return context


        
# class FragrancesList1(ListView):
#     model = FragrancesModel
#     template_name = 'dashboard1.html'
#     context_object_name = 'fragrance_list'  # esta categoria renombra objetc_list por un nombre mas legible
#     paginate_by = 3
#
# # In this section I am adding the filter as a context and it passes to the template
#     def get_context_data(self, **kwargs):
#         context=super().get_context_data(**kwargs)
#         context['fragrance_filter'] = FragranceFilter(self.request.GET, queryset=self.get_queryset() )
#         return context



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
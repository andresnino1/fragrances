from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, View
from .models import FragrancesModel
from .filters import FragranceFilter
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin




# Create your views here.

# This view back to home
class HomePageView(TemplateView):
    template_name = 'home.html'


# This view return the list of fragrances in dashboard
class FragrancesList(LoginRequiredMixin,ListView):
    model = FragrancesModel
    template_name = 'dashboard.html'
    context_object_name = 'fragrance_list'  # this cathegory rename object_list for a better name 'fragrance list'
    paginate_by = 3

# In this section I am adding the filter as a context and it passes to the template
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['fragrance_filter'] = FragranceFilter(self.request.GET, queryset=self.get_queryset() )
        return context


        

# this view return the website detail of each fragrance

class FragrancesDetailView(LoginRequiredMixin,DetailView):
    model = FragrancesModel
    context_object_name = 'fragrance_detail'
    template_name = 'fragrances-detail.html'


# this class check if the user is supper user in order to allow the view
class SuperUserCheck(UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_superuser


# this view is a form to add new fragrances in database

class AddFragrancesView(LoginRequiredMixin,SuperUserCheck, CreateView):
    model = FragrancesModel
    context_object_name = 'create_fragrance'
    fields = '__all__'
    template_name = "addfragrance.html"
    #success_url = reverse_lazy('dashboard')





# this view will handle the user registration on the application
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'registration/signup.html'


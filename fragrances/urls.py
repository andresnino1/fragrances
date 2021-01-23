from django.urls import path
from fragrances.views import HomePageView, FragrancesList, FragrancesDetailView, AddFragrancesView, SignUpView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('dashboard/', FragrancesList.as_view(), name='dashboard'),
    path('addfragrance/', AddFragrancesView.as_view(), name='add_fragrance'),
    path('fragrance/<int:pk>', FragrancesDetailView.as_view(), name='fragrance_detail'),
    path('signup/', SignUpView.as_view(), name='signup'),

]

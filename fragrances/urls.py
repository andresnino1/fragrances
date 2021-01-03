from django.urls import path
from fragrances.views import HomePageView, FragrancesList, DashBoardView, FragrancesDetailView, AddFragrancesView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('dashboard/', FragrancesList.as_view(), name='dashboard'),
    path('addfragrance/', AddFragrancesView.as_view(), name='add_fragrance'),
    path('fragrance/<int:pk>', FragrancesDetailView.as_view(), name='fragrance_detail'),
]

from django.urls import path
from fragrances.views import HomePageView, FragrancesList, DashBoardView, FragrancesDetailView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('dashboard/', FragrancesList.as_view(), name='dashboard'),
    path('fragrance/<int:pk>', FragrancesDetailView.as_view(), name='fragrance_detail'),
]

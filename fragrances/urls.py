from django.urls import path
from fragrances.views import HomePageView, FragrancesList, DashBoardView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('dashboard/', FragrancesList.as_view(), name='dashboard'),
]

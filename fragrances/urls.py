from django.urls import path
from fragrances.views import HomePageView, DashBoardView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('dashboard/', DashBoardView.as_view(), name='dashboard'),
]

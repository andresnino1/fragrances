import django_filters
from django import forms
from .models import *


class FragranceFilter(django_filters.FilterSet):
    # fragrance_code = django_filters.CharFilter(field_name="fragrance_code", lookup_expr='icontains', label='codigo',
    #                                            widget=forms.TextInput(
    #                                                attrs={'class': 'form-control', 'placeholder': 'code',
    #                                                       'lable': 'code'}))
    # commecial_name = django_filters.CharFilter(field_name="commercial_name", lookup_expr='icontains',
    #                                            label='commercial name',
    #                                            widget=forms.TextInput(
    #                                                attrs={'class': 'form-control', 'placeholder': 'commercial name'}))

    class Meta:
        model = FragrancesModel
        fields = ('fragrance_code', 'commercial_name')

        fields = {
            'fragrance_code': ['icontains'],
            'commercial_name': ['icontains'],
        }

        # widgets = {
        #     'fragrance_code': forms.TextInput(attrs={'class': 'input', 'placeholder': 'fragrance code'}),
        #     'commercial_name': forms.TextInput(attrs={'class': 'input', 'placeholder': 'commercial name'}),
        #
        # }

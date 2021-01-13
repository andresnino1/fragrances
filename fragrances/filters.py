import django_filters
from django import forms
from .models import *


class FragranceFilter(django_filters.FilterSet):
    fragrance_code = django_filters.CharFilter(field_name="fragrance_code", lookup_expr='icontains', )
    commercial_name = django_filters.CharFilter(field_name="commercial_name", lookup_expr='icontains',  )
    #the next filter search on commentsmodel for the comment
    commentsmodel__comment=django_filters.CharFilter(lookup_expr='icontains',)

    class Meta:
        model = FragrancesModel
        fields = ['fragrance_code','application', 'commercial_name','first_family', 'second_family','third_family',
                  'nota_salida','nota_cuerpo','nota_fondo', 'market_type', 'technology', 'collection_prom',
                  'natural_extracts', 'essential_club', 'vigente', 'shortlisted', 'won_selling', 'natural_derived',
                  'ecocert', 'bio_degradable', 'dangerous_good', 'ai', 'commentsmodel__comment',
                  ]

            

from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)

    # def __str__(self):
    #    return self.name


class ApplicationModel(models.Model):
    application_name = models.CharField(max_length=20)

    def __str__(self):
        return self.application_name


class FirstFamilyModel(models.Model):
    first_family = models.CharField(max_length=20)

    def __str__(self):
        return self.first_family


class SecondFamilyModel(models.Model):
    second_family = models.CharField(max_length=20)

    def __str__(self):
        return self.second_family


class ThirdFamilyModel(models.Model):
    third_family = models.CharField(max_length=20)

    def __str__(self):
        return self.third_family


class TechnologyModel(models.Model):
    technology = models.CharField(max_length=20)

    def __str__(self):
        return self.technology


class CollectionModel(models.Model):
    collection = models.CharField(max_length=20)

    def __str__(self):
        return self.collection


class NaturalExtractsModel(models.Model):
    natural_extracts = models.CharField(max_length=20)

    def __str__(self):
        return self.natural_extracts


class MarketTypeModel(models.Model):
    market_type = models.CharField(max_length=20)

    def __str__(self):
        return self.market_type


class NotaSalidaModel(models.Model):
    nota_salida = models.CharField(max_length=20)

    def __str__(self):
        return self.nota_salida


class NotaCuerpoModel(models.Model):
    nota_cuerpo = models.CharField(max_length=20)

    def __str__(self):
        return self.nota_cuerpo


class NotaFondoModel(models.Model):
    nota_fondo = models.CharField(max_length=20)

    def __str__(self):
        return self.nota_fondo


class FragrancesModel(models.Model):
    fragrance_code = models.CharField(max_length=20)
    essential_club = models.BooleanField()
    vigente = models.BooleanField()
    application = models.ManyToManyField(ApplicationModel)  # Relation Many to Many (it is like a TAG)
    commercial_name = models.CharField(max_length=20)
    box = models.IntegerField()
    cost_kilo_us = models.FloatField()
    selling_price_aud = models.FloatField()
    first_family = models.ManyToManyField(FirstFamilyModel)  # Relation Many to Many (it is like a TAG)
    second_family = models.ManyToManyField(SecondFamilyModel)  # Relation Many to Many (it is like a TAG)
    third_family = models.ManyToManyField(ThirdFamilyModel)  # Relation Many to Many (it is like a TAG)
    market_type = models.ManyToManyField(MarketTypeModel)  # Relation Many to Many (it is like a TAG)
    nota_salida = models.ManyToManyField(NotaSalidaModel)  # Relation Many to Many (it is like a TAG)
    nota_cuerpo = models.ManyToManyField(NotaCuerpoModel)  # Relation Many to Many (it is like a TAG)
    nota_fondo = models.ManyToManyField(NotaFondoModel)  # Relation Many to Many (it is like a TAG)
    expiry_date = models.DateField()
    sample_size = models.FloatField()
    technology = models.ManyToManyField(TechnologyModel)  # Relation Many to Many (it is like a TAG)
    collection_prom = models.ManyToManyField(CollectionModel)  # Relation Many to Many (it is like a TAG)
    shortlisted = models.BooleanField()
    won_selling = models.BooleanField()
    natural_extracts = models.ManyToManyField(NaturalExtractsModel)  # Relation Many to Many (it is like a TAG)
    allergen = models.FloatField()
    natural_percentage = models.BooleanField()
    natural_derived = models.BooleanField()
    ecocert = models.BooleanField()
    bio_degradable = models.BooleanField()
    dangerous_good = models.BooleanField()
    ai = models.BooleanField()

    # user_comment = models.ManyToManyField(CommentsModel)  # Relation Many to Many (it is like a TAG)

    def __str__(self):
        return self.fragrance_code


class CommentsModel(models.Model):
    comment = models.TextField()
    # el campo author on_delete, si se borra un author el comentario queda en la BD
    author = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    fragrance = models.ForeignKey(FragrancesModel, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.author)

from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


# Create your models here.

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True, verbose_name="edad")

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
    fragrance_code = models.CharField(unique=True, max_length=20, verbose_name="fragrance code")
    essential_club = models.BooleanField(verbose_name="essential club", default=False, null=False)
    vigente = models.BooleanField(verbose_name="vigente")
    application = models.ManyToManyField(ApplicationModel, verbose_name="application")  # Relation Many to Many (it is like a TAG)
    commercial_name = models.CharField(max_length=20, verbose_name="commercial name")
    box = models.IntegerField(verbose_name="box")
    cost_kilo_us = models.FloatField(verbose_name="cost kilo")
    selling_price_aud = models.FloatField(verbose_name="selling price")
    first_family = models.ManyToManyField(FirstFamilyModel, verbose_name="first")  # Relation Many to Many (it is like a TAG)
    second_family = models.ManyToManyField(SecondFamilyModel, verbose_name="second family")  # Relation Many to Many (it is like a TAG)
    third_family = models.ManyToManyField(ThirdFamilyModel, verbose_name="third family")  # Relation Many to Many (it is like a TAG)
    market_type = models.ManyToManyField(MarketTypeModel, verbose_name="market type")  # Relation Many to Many (it is like a TAG)
    nota_salida = models.ManyToManyField(NotaSalidaModel, verbose_name="nota salida")  # Relation Many to Many (it is like a TAG)
    nota_cuerpo = models.ManyToManyField(NotaCuerpoModel, verbose_name="nota cuerpo")  # Relation Many to Many (it is like a TAG)
    nota_fondo = models.ManyToManyField(NotaFondoModel, verbose_name="nota fondo")  # Relation Many to Many (it is like a TAG)
    expiry_date = models.DateField(verbose_name="expiry date")
    sample_size = models.FloatField(verbose_name="sample size")
    technology = models.ManyToManyField(TechnologyModel, verbose_name="technology")  # Relation Many to Many (it is like a TAG)
    collection_prom = models.ManyToManyField(CollectionModel, verbose_name="collection")  # Relation Many to Many (it is like a TAG)
    shortlisted = models.BooleanField(verbose_name="shortlisted")
    won_selling = models.BooleanField(verbose_name="won selling")
    natural_extracts = models.ManyToManyField(NaturalExtractsModel, verbose_name="natural extracts")  # Relation Many to Many (it is like a TAG)
    allergen = models.FloatField(verbose_name="allergen")
    natural_percentage = models.BooleanField(verbose_name="natural percentage")
    natural_derived = models.BooleanField(verbose_name="natural derived")
    ecocert = models.BooleanField(verbose_name="ecocert")
    bio_degradable = models.BooleanField(verbose_name="bio degradable")
    dangerous_good = models.BooleanField(verbose_name="dangerous good")
    ai = models.BooleanField(verbose_name="ai")


    # user_comment = models.ManyToManyField(CommentsModel)  # Relation Many to Many (it is like a TAG)

    def __str__(self):
        return self.fragrance_code

# after success form submit get_absolute_url will return to the fragrance detail url
    def get_absolute_url(self):
        return reverse('fragrance_detail', args=[str(self.id)])


class CommentsModel(models.Model):
    comment = models.TextField()
    # el campo author on_delete, si se borra un author el comentario queda en la BD
    author = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, verbose_name="author")
    fragrance = models.ForeignKey(FragrancesModel, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.author)

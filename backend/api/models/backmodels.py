from re import A
import time
from django.db import models


class Bachelier(models.Model):
    numero_iscription = models.IntegerField()
    session = models.DateField()
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=100, null=True, blank=True)
    date_naissance = models.DateField()
    lieu_naissance = models.CharField(max_length=100)
    pays_de_naissance = models.CharField(max_length=50, default="MADAGASCAR")
    serie = models.CharField(
        max_length=3,
        choices=[
            ("A1", "A1"),
            ("A2", "A2"),
            ("C", "C"),
            ("D", "D"),
            ("OSE", "OSE"),
            ("L", "L"),
            ("S", "S"),
        ],
    )
    mention = models.CharField(
        max_length=50,
        choices=[
            ("PASSABLE", "PASSABLE"),
            ("ASSEZ-BIEN", "ASSEZ-BIEN"),
            ("BIEN", "BIEN"),
            ("TRES-BIEN", "TRES-BIEN"),
        ],
    )
    numero_ordre = models.CharField(max_length=50, null=True, blank=True)
    releve_note_obtenu = models.BooleanField(default=False)
    Diplome_obtenu = models.BooleanField(default=False)
    date_obtention = models.DateField(auto_now=True)


class DemandeDeDiplome(models.Model):
    date_demande = models.DateTimeField(auto_now_add=True)
    num_bacc = models.IntegerField()
    reference_banque = models.CharField(max_length=100)
    lieu_recuperation = models.CharField(
        max_length=50,
        choices=[
            ("ANTANANARIVO", "ANTANANARIVO"),
            ("ANTSIRANANA", "ANTSIRANANA"),
            ("MAHAJANGA", "MAHAJANGA"),
            ("TOAMASINA", "TOAMASINA"),
            ("TOLIARA", "TOLIARA"),
            ("FIANARATSOA", "FIANARATSOA"),
        ],
    )
    fini = models.BooleanField(default=False)
    livre = models.BooleanField(default=False)

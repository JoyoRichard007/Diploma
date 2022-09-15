import time
from django.db import models


class Etudiant(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=100)
    date_naissance = models.DateField()
    date_naissance = models.DateField()
    lieu_naissance = models.CharField(max_length=100)
    pays_de_naissance = models.CharField(max_length=50, default="MADAGASCAR")
    pere = models.CharField(max_length=150, null=True, blank=True)
    mere = models.CharField(max_length=150, null=True, blank=True)
    num_cin = models.CharField(max_length=15, null=True, blank=True)
    adresse = models.CharField(max_length=150)
    num_telephone = models.CharField(max_length=20)

    def image_filename(instance, filename):
        extension = filename.split(".")[-1]
        specifique = str(time.time())
        new_filename = f"photo_{instance.nom}_{instance.prenom}_{instance.num_cin}_{specifique}.{extension}"
        return new_filename

    photo = models.ImageField(
        upload_to=image_filename,
        null=True,
        blank=True,
    )
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom + " " + self.prenom


class TraceEtude(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    niveau = models.CharField(
        max_length=10,
        choices=[
            ("L1", "LICENCE 1"),
            ("L2", "LICENCE 2"),
            ("L3", "LICENCE 3"),
            ("M1", "MASTER 1"),
            ("M2", "MASTER 2"),
        ],
    )
    filiere = models.CharField(max_length=100)
    annee_universitaire = models.CharField(max_length=15)
    universite = models.CharField(max_length=50)
    lieu_universite = models.CharField(max_length=50)
    pays = models.CharField(max_length=50)
    moyenne = models.IntegerField(null=True, blank=True)
    date_created_niveau = models.DateTimeField(auto_now=True)


class DiplomeLMD(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    niveau = models.CharField(
        max_length=10,
        choices=[
            ("LICENCE", "LICENCE"),
            ("MASTER", "MASTER"),
            ("DOCTORAT", "DOCTORAT"),
        ],
    )
    date_creation = models.DateField()
    date_obtention = models.DateField()
    obtenu = models.BooleanField(default=False)

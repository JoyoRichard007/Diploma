from .models import *
from django.contrib import admin


class UserAdminAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "username",
        "email",
        "password",
        "province",
        "is_superuser",
    )


class DemandeDeDiplomeAdmin(admin.ModelAdmin):
    list_display = (
        "date_demande",
        "num_bacc",
        "reference_banque",
        "lieu_recuperation",
        "fini",
        "livre",
    )


class BachelierAdmin(admin.ModelAdmin):
    list_display = (
        "numero_iscription",
        "session",
        "nom",
        "prenom",
        "serie",
        "mention",
        "numero_ordre",
        "Diplome_obtenu",
    )


class EtudiantAdmin(admin.ModelAdmin):
    list_display = ("id", "date_created", "nom", "prenom", "adresse", "num_telephone")


class TraceEtudeAdmin(admin.ModelAdmin):
    list_display = (
        "etudiant",
        "date_created_niveau",
        "niveau",
        "filiere",
        "annee_universitaire",
        "universite",
    )


class DiplomeLMDAdmin(admin.ModelAdmin):
    list_display = ("etudiant", "niveau", "obtenu")


admin.site.register(Etudiant, EtudiantAdmin)
admin.site.register(UserAdmin, UserAdminAdmin)
admin.site.register(Bachelier, BachelierAdmin)
admin.site.register(TraceEtude, TraceEtudeAdmin)
admin.site.register(DiplomeLMD, DiplomeLMDAdmin)
admin.site.register(DemandeDeDiplome, DemandeDeDiplomeAdmin)

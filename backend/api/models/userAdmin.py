import time
from django.db import models
from django.contrib.auth.models import AbstractUser


class UserAdmin(AbstractUser):
    province = models.CharField(
        max_length=20,
        choices=[
            ("ANTANANARIVO", "ANTANANARIVO"),
            ("ANTSIRANANA", "ANTSIRANANA"),
            ("MAHAJANGA", "MAHAJANGA"),
            ("TOAMASINA", "TOAMASINA"),
            ("TOLIARA", "TOLIARA"),
            ("FIANARATSOA", "FIANARATSOA"),
        ],
    )

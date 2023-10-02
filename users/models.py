from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
    Represents a user in the system.

    Inherits from the AbstractUser model provided by Django.
    """

    last_name = models.CharField(_("last name"), max_length=255)
    first_name = models.CharField(_("first name"), max_length=255, blank=True)
    birth_date = models.DateField(_("birth date"), null=True, blank=True)

    SEXE_CHOICES = (
        ("M", "Masculin"),
        ("F", "Féminin"),
        ("A", "Autre"),
    )
    sexe = models.CharField(_("sexe"), max_length=1, choices=SEXE_CHOICES)
    phone = models.CharField(_("phone"), max_length=15)
    bio = models.TextField(_("bio"), blank=True)

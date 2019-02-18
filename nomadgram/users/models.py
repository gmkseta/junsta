from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):


    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('not-specified', 'Not sepecified')
    )

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    website = models.URLField(_(""), max_length=200, null=True)
    bio = models.TextField(_(""), null=True)
    phone = models.CharField(_(""), max_length=50, null=True)
    gender = models.CharField(_(""), max_length=80, choices=GENDER_CHOICES, null=True)
    followers = models.ManyToManyField("self", verbose_name=_(""))
    following = models.ManyToManyField("self", verbose_name=_(""))





    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})

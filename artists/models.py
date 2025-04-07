from django.db import models

import pycountry

COUNTRY_CHOICES = [(p.alpha_2, p.name) for p in pycountry.countries]

# Create your models here.
class Artist(models.Model):
    name = models.TextField(unique=True)
    country = models.CharField(max_length=2, choices=COUNTRY_CHOICES)

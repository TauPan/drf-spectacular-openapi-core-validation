from django.contrib import admin
from django.core.validators import RegexValidator
from django.db import models

import pycountry

COUNTRY_CHOICES = [(p.alpha_2,
                    p.name) for p in pycountry.countries]

# Create your models here.
class Artist(models.Model):
    name = models.TextField(unique=True)
    country = models.CharField(
        max_length=2, choices=COUNTRY_CHOICES)
    slug_id = models.CharField(
        unique=True,
        help_text=(
            'A (possibly empty) name in lower case asci alphabet letters'
            ' or underscores [a-z_] followed by an 8 digit lowercase hex'
            ' number. (e.g.: "the_the-e461ca37")'),
        max_length=32,
        validators=[RegexValidator(r'[a-z_]{0,23}-[0-9a-f]{8}')])

    def __str__(self):
        return f'{self.name} ({self.country})'


admin.site.register(Artist)

from django.db import models
from . import shorting

# Create your models here.
class ShortUrl(models.Model):
    url = models.CharField(max_length=255, default='', unique=True)
    short_url = models.CharField(max_length=255, default='', blank=True)
    create_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.short_url

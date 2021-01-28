from django.db import models
from django.conf import settings


class Entry(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    email = models.EmailField(verbose_name="email", max_length=60)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=80)
    notes = models.TextField(max_length=300, null=True, blank=True)
    site_name = models.CharField(max_length=30)
    site_url = models.CharField(max_length=80)
    last_edited = models.DateField(auto_now=True)
    date_created = models.DateField(auto_now_add=True)
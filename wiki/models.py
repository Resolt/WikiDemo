from django.db import models
from django.urls import reverse


class WikiPage(models.Model):
    title = models.CharField(max_length=256)
    text = models.CharField(max_length=2048)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("wiki:detail", kwargs={'pk':self.pk})
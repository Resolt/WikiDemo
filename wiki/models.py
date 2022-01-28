from django.db import models
from django.urls import reverse


class WikiPage(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=2000)
    links = models.JSONField(default=dict)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("wiki:detail", kwargs={'pk':self.pk})

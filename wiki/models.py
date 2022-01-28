from django.db import models
from django.urls import reverse


class WikiPage(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=2000)
    links = models.ManyToManyField("wiki.WikiPage", verbose_name="Links")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("wiki:detail", kwargs={'pk':self.pk})

    @property
    def url(self):
        return self.get_absolute_url()

    @property
    def get_links(self):
        return self.links.all()

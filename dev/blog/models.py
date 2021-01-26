from django.db import models
from django.urls import reverse
# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=120, default='Title')
    content = models.TextField(default='Content')
    active = models.BooleanField(default=True)

    def get_absolute_url(self):
        # Takes you to URL after inputting data
        return reverse('articles:articles-detail', kwargs={'id': self.id})

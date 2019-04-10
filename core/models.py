from django.db import models
from datetime import datetime
# from taggit.managers import TaggableManager
from martor.models import MartorField
from django.utils import timezone


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=500, null=False, blank=False)
    content = MartorField()
    categories = models.ManyToManyField('Category')
    published_date = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(max_length=250)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title




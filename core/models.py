from django.db import models
from datetime import datetime
from taggit.managers import TaggableManager


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=500, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    tags = TaggableManager()
    published_date = models.DateTimeField(null=True, blank=True)
    slug = models.SlugField(max_length=250)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title




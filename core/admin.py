from django.contrib import admin
from django.db import models
from core.models import Post, Category


admin.site.register(Category)
admin.site.register(Post)

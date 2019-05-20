from django.contrib import admin
from django.db import models
from core.models import Post, Category


# # Register your models here.
# class PostAdmin(admin.ModelAdmin):
#     prepopulated_fields = {'slug': ('title',)}
#     # formfield_overrides = {
#     #     models.TextField: {'widget': AdminMartorWidget},
#     # }


admin.site.register(Category)
admin.site.register(Post)

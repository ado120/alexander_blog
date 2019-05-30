from django.urls import path,include
from core import views

urlpatterns = [
    path('', views.blog_index, name='blog_index'),
    path('<slug>-<pk>', views.post_view, name='post_view'),
    path('reviews', views.current_datetime, name='current_datetime')
]
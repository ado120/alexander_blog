from django.urls import path,include
from landing_page import views

urlpatterns = [
    path('', views.landing_page, name='landing_page')
]
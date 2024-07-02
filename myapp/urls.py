from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('date', views.display_date, name='display_date'),
]

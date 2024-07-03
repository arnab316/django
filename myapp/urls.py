from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('date', views.display_date, name='display_date'),
    path('showform/', views.showform, name="showform"),
    path("showform/getform/", views.getform, name='getform'),
    path('dishes/<str:dish>', views.menuitems, name='dishes'),

]

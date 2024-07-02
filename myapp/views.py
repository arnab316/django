from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


# Create your views here.
def home(request):
    return HttpResponse('Welcome to little Lemon website')


def display_date(request):
    date_val = datetime.now().year
    return HttpResponse(date_val)

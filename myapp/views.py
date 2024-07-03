from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


# Create your views here.
def home(request):
    path = request.path
    scheme = request.scheme
    method = request.method
    address = request.META['REMOTE_ADDR']
    user_agent = request.META['HTTP_USER_AGENT']
    path_info = request.path_info
    msg = f"""<br>
    <br> Path: {path}
    <br> Address: {address}
    <br> Scheme: {scheme}
    <br> Method: {method}
    <br> User_agent: {user_agent}
    <br> Path info : {path_info}
    """
    return HttpResponse(msg, content_type='text/html', charset='utf-8')


def display_date(request):
    date_val = datetime.now().year
    return HttpResponse(date_val)

def getform(request):
    if request.method == "POST":
        id=request.POST['id']
        name=request.POST['name']
    return HttpResponse("Name:{} UserID:{}".format(name, id))
def showform(request):
    return render(request, "form.html")



def menuitems(request, dish):
    items = {
        'pasta': 'the test files here are',
        'falafal': 'the middle east dish',
        'cheesecake': 'milk items here are',
    }
    desc = items[dish]
    return HttpResponse(f'<h2>{dish}</h2>' + desc)
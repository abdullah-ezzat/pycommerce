from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.


def welcome(request):
    return render(request, 'welcome.html')

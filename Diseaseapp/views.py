from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Home_Page(Request):
    return render(Request,   'Diseaseapp/Home_Page.html')


def Main_Page(Request):
    return  render(Request, 'Diseaseapp/Main_Page.html',{'ans':'images/logistic.jpeg'})

def Logistic(Request):
    return render(Request, 'Diseaseapp/Logistic.html')
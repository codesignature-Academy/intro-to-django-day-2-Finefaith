from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return HttpResponse('<h1>Welcome to Faithcompany\'s website 💇‍♀️</h1>')

def about(request):
    return HttpResponse('We serve you the best hairs💇‍♀️, cosmetics💕, nails💅 and lashes. Send a DM')

def contact(request):
    return HttpResponse('contact us : 📩ubanifaith2000@gmail.com')

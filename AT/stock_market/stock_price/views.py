from django.shortcuts import render, redirect
from .models import Company
from django.db.models import F #Basically does arithmetic with stuff in the database.
"""
We use Jinja templating in the html templates.
"""


#views.home
def home(request):
    percentage_change = Company.objects.all().annotate(diff = F('current_price')- F('opening_price')) #updating the percentage change
    context = {
    'details': Company.objects.all()  #Sending data so that the html template can use it.
    }
    #This particular file structure is required in django, although it may seem weird.
    return render(request,'stock_price/home.html',context)#go to stock_price/templates/stock_price/home.html.



def about(request):
    return render(request,'stock_price/about.html')

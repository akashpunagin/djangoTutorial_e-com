from django.shortcuts import render
from django.http import HttpResponse
# from .models import Product,Contact,Order

def index(request):
    return render(request, 'index.html')

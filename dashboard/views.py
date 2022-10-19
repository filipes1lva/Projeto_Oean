from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return render(request, 'dashboard/index.html')
    #return HttpResponse('<h1 style="color:blue;"> Esta é a página de index </h1>')

def staff(request):
    return render(request, 'dashboard/staff.html')

def products(request):
    return render(request, 'dashboard/products.html')

def order(request):
    return render(request, 'dashboard/order.html')

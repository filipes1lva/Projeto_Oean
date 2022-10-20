from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required



# Create your views here.


@login_required
def index(request):
    return render(request, 'dashboard/index.html')
    #return HttpResponse('<h1 style="color:blue;"> Esta é a página de index </h1>')

@login_required
def staff(request):
    return render(request, 'dashboard/staff.html')

@login_required
def products(request):
    return render(request, 'dashboard/products.html')

@login_required
def order(request):
    return render(request, 'dashboard/order.html')

from django.shortcuts import render
from .models import Product
from .forms import ProductForm

# Create your views here.

def Index(request):
    if request.method == "POST":
        fm = ProductForm(request.POST,request.FILES)
        print(fm)
        if fm.is_valid():
            fm.save()
            fm = ProductForm()
    else:
        fm = ProductForm()
    return render(request,'index.html',{'form':fm})

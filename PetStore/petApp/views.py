from django.shortcuts import render, HttpResponseRedirect
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
            return HttpResponseRedirect('/display/')
    else:
        fm = ProductForm()
    return render(request,'index.html',{'form':fm})

def Display(request):
    data = Product.objects.all()
    print(data)
    return render(request,'display.html',{'data':data})

def Delete(request,id):
    if request.method == "POST":
        ## print(id)
        os = Product.objects.get(pk=id)
        os.delete()
        return HttpResponseRedirect('/display/')

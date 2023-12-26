from django.shortcuts import render, HttpResponseRedirect
from .models import Product
from .forms import ProductForm
from django.contrib import messages

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
        messages.success(request,"Data Deleted Succeessfully")
        return HttpResponseRedirect('/display/')

def Update(request,id):
    if request.method == "POST":
        os = Product.objects.get(pk=id)
        fm = ProductForm(request.POST, request.FILES, instance=os)
        if fm.is_valid():
            fm.save()
            messages.success(request,"Data Updated Succesfully")
            return HttpResponseRedirect('/display/')
    else:
        os = Product.objects.get(pk=id)
        # print(os)
        fm = ProductForm(instance=os)
    return render(request, 'update.html',{'Updateform':fm})

def UserBase(request):
    return render(request,'user/base.html')

def UserIndex(request):
    data = Product.objects.all()
    return render(request,'user/index.html',{'data':data})
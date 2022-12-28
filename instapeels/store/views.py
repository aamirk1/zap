from django.shortcuts import render
from django.contrib import messages
from .models import *   
# Create your views here.
def home(request):
    return render(request, 'store/index.html')

def collection(request):
    ne = Category.objects.filter(status=0)
    context = {'ne':ne}
    return render(request, 'store/collection.html',context)

def shop(request):
    pro = Product.objects.filter(status = 0)
    context = {'pro':pro}
    return render(request, 'store/shop.html',context)

def collectionview(request,slug):
    if(Category.objects.filter(slug=slug,status=0)):
        products = Product.objects.filter(category_slug=slug)
        category_name = Category.objects.filter(slug=slug).first()
        context = {'products':products,'category_name':category_name}
        return render(request, 'store/products/index.html',context)
    else:
        messages.warning(request, 'No Such Category found!')
        return redirect('collection')
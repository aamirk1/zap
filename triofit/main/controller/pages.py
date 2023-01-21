from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from main.models import Category, Product
# Create your views here.
def aboutus(request):
    return render(request, 'main/navbarpages/aboutus.html')

def gallery(request):
    return render(request, 'main/navbarpages/gallery.html')
    
def ThirdPartyManufac(request):
    return render(request, 'main/navbarpages/tpm.html')
    
def contactus(request):
    return render(request, 'main/navbarpages/contactus.html')
    
def events(request):
    return render(request, 'main/navbarpages/events.html')

def productrange(request):
    return render(request, 'main/navbarpages/productrange.html')
    
def triofit(request):
    # if(Category.objects.filter(slug=slug,status=0)):
    #     products = Product.objects.filter(category__slug=slug)
    #     category = Category.objects.filter(slug=slug).first()
    #     context = {'products':products,'category':category}
    return render(request, 'main/navbarpages/triofit.html')
    
    # else:
    #     messages.warning(request, 'No Such Category found!')
    #     return redirect('home')

    
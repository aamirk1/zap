from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from main.models import Category, Product

from django.http import HttpResponseRedirect
from main.forms import ContactForm
# Create your views here.
def aboutus(request):
    return render(request, 'main/navbarpages/aboutus.html')

def gallery(request):
    return render(request, 'main/navbarpages/gallery.html')
    
def ThirdPartyManufac(request):
    return render(request, 'main/navbarpages/tpm.html')
    
def contactus(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contactus')
    else:
        form = ContactForm()
    return render(request, 'main/navbarpages/contactus.html', {'form': form})


    
def events(request):
    return render(request, 'main/navbarpages/events.html')

def productrange(request):
    return render(request, 'main/navbarpages/productrange.html')
    
   
def triofit(request):
    new = Category.objects.filter(status=0)
    pro = Product.objects.filter(status=0)
    context = {'pro':pro,'new':new}
    return render(request, 'main/navbarpages/triofit.html',context)
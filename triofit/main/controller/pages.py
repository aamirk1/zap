from django.shortcuts import render

# Create your views here.
def aboutus(request):
    return render(request, 'main/navbarpages/aboutus.html')

def gallery(request):
    return render(request, 'main/navbarpages/gallery.html')
    
def ThirdPartyManufac(request):
    return render(request, 'main/navbarpages/tpm.html')
    
def contactus(request):
    return render(request, 'main/navbarpages/contactus.html')

    
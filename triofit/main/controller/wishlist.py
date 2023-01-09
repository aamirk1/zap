from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.contrib import messages 
from main.models import Wishlist,Product

@login_required(login_url='loginpage')
def index(request):
    wishlist = Wishlist.objects.filter(user=request.user)
    context = {'wishlist':wishlist}
    return render(request,'main/wishlist.html', context)

def addtowishlist(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id= int(request.POST.get('product_id'))
            product_check = Product.objects.get(id=prod_id)
            if (product_check):
                if(Wishlist.objects.filter(user=request.user.id,product_id=prod_id)):
                    return JsonResponse({'status':"Product Is Already In Wishlist"})
                else:
                    Wishlist.objects.create(user=request.user,product_id=prod_id)
                    return JsonResponse({'status':"Product added successfully"})
            else:
                return JsonResponse({'status':"No Such Product Found"})
        else:
            return JsonResponse({'status':"Login To Continue!"})

    return render(request,'/')

def deletewishlistitem(request):
    if request.method =='POST':
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))
            if(Wishlist.objects.filter(user=request.user,product_id=prod_id)):
                wishlistitem=Wishlist.objects.get(product_id= prod_id,user=request.user)
                wishlistitem.delete()
                return JsonResponse({'status':"Product remove from wishlist"})
            else:
                return JsonResponse({'status':"Product not found in wishlist"})
        else:
            return JsonResponse({'status':"Login to continue"})
    return redirect('/')

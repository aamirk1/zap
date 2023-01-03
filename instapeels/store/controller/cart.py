from django.contrib.auth import authenticate,login
from django.shortcuts import render,redirect
from django.contrib import messages 
from store.models import Product,Cart

def addtocart(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id= int(request.POST.get('product_id'))
            product_check = Product.objects.get(id=prod_id)
            if (product_check):
                if(Cart.objects.filter(user=request.user.id,product_id=prod_id)):
                    return JsonResponse({'status':"Product Is Already In Cart"})
                else:
                    prod_qty = int(request.POST.get('product_qty'))
                    if product_check.quantity >= prod_qty:
                        Cart.objects.create(user=request.user.id,product_id=prod_id,product_qty= prod_qty)
                        return JsonResponse({'status':"Product added successfully"})
                    else:
                        return JsonResponse({'status':"Only "+ str(product_check.quantity)+" quantity available"})
            else:
                return JsonResponse({'status':"No Such Product Found"})
        else:
            return JsonResponse({'status':"Login To Continue!"})

    return render(request,'/')
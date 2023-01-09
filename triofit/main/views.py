from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'main/index.html')


def collection(request):
    ne = Category.objects.filter(status=0)
    context = {'ne':ne}
    return render(request, 'main/collection.html',context)


def collectionview(request,slug):
    if(Category.objects.filter(slug=slug,status=0)):
        products = Product.objects.filter(category__slug=slug)
        category = Category.objects.filter(slug=slug).first()
        context = {'products':products,'category':category}
        return render(request, 'main/products/index.html',context)
    else:
        messages.warning(request, 'No Such Category found!')
        return redirect('collection')

def productview(request,cate_slug,prod_slug):
    if(Category.objects.filter(slug=cate_slug,status=0)):
        if(Product.objects.filter(slug=prod_slug,status=0)):
            products = Product.objects.filter(slug=prod_slug,status=0).first()
            context = {'products':products}
        else:
            messages.error(request,'No Such Product Found')
            # return redirect('collection')
    else:
        messages.error(request,'No Such Category Found')
        return redirect('collection')
    return render(request, 'main/products/view.html',context)
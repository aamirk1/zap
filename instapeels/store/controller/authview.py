from django.contrib.auth import authenticate,login
from django.shortcuts import render,redirect
from django.contrib import messages 
from store.forms import CustomUserForm
def register(request):
    form = CustomUserForm()
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Registration Successfull')
            return redirect('login/')
    context = {'form':form}
    
    return render(request, 'store/auth/register.html',context)
    
def loginpage(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        passwd = request.POST.get('password')
        user = authenticate(request,username=name,password=passwd)

        if user is not none:
            login(request,user)
            messages.success(request,"Logged in Successfully")
            return redirect("/")
        else:
            messages.error(request,"Invalid Username or Password")
            return redirect("/login")
    return render(request, 'store/auth/login.html')

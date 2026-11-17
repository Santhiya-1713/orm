from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import UserCreationForm
from .forms import UserForm
# Create your views here.
def my_view(request):
    context={'logo_url':'img/logo.webp'}
    return render(request,'index.html',context)
def home(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is None:
            return redirect('/')
        login(request,user)
        return render(request,'welcome.html',{'logo_url':'img/logo.webp'})
    else:
        form=UserForm()
        return render(request,'index.html',{'form':form,'logo_url':'img/logo.webp'})
def showwelcome(request):
    return render(request,'welcome.html',{'logo_url':'img/logo.webp'})
def register(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('/welcome')
    else:
        form=UserCreationForm()
        return render(request,'register.html',{'form':form,'logo_url':'img/logo.webp'})
def logoutme(request):
    logout(request)
    return redirect('/')
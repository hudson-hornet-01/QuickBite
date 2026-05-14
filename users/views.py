from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth import logout
# Create your views here.
def register(request):
    form = RegisterForm(request.POST or None)
    if request.method=="POST":
        if form.is_valid():
            form.save()
            firstname = form.cleaned_data.get('first_name')
            messages.success(request,f'Welcome {firstname}, your account has been successfully created')
            return redirect('users:login')
    context = {
        'form':form
    }
    return render(request,'users/register.html',context) 

def logout_view(request):
    logout(request)
    
    return render(request,'users/logout.html')
from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import RegisterForm
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
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.
def register(request):
    form = UserCreationForm(request.POST or None)
    if request.method=="POST":
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Welcome {username},your account has been successfully created')
            return redirect('Food:index')
    context = {
        'form':form
    }
    return render(request,'users/register.html',context) 
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def register(request):
    form = UserCreationForm(request.POST or None)
    if request.method=="POST":
        if form.is_valid():
            form.save()
            return redirect('Food:index')
    context = {
        'form':form
    }
    return render(request,'users/register.html',context) 
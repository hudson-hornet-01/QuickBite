from django.shortcuts import render,redirect
from .models import Item
from .forms import ItemForm
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView

# Create your views here.
# @login_required
# def index(request):
#     item_list = Item.objects.all()
#     context = {
#         'item_list': item_list,
#     }
#     return render(request, 'Food/index.html', context)

class IndexClassView(ListView):
    model = Item
    template_name = 'Food/index.html'
    context_object_name = 'item_list'

def detail(request,id):
    item = Item.objects.get(pk=id)
    context = {
        'item':item,
    }
    return render(request,'Food/detail.html',context)

def create_item(request):
    form = ItemForm(request.POST or None)
    if request.method=="POST":
        if form.is_valid():
            form.save()
            return redirect("Food:index")
        
    context = {
        'form' : form,
    }
    return render(request,'food/item-form.html',context)

def update_item(request,id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None,instance=item)
    
    if form.is_valid():
        form.save()
        return redirect("Food:index")
    
    context = {
        'form':form
    }
    
    return render(request, 'Food/item-form.html',context)

def delete_item(request,id):
    item = Item.objects.get(id=id)
    if request.method=='POST':
        item.delete()
        return redirect('Food:index')
    
    return render(request, 'Food/item-delete.html')
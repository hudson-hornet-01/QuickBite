from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm

# Create your views here.
def index(request):
    item_list = Item.objects.all()
    context = {
        'item_list': item_list,
    }
    return render(request, 'Food/index.html', context)

def item(request):
    return HttpResponse("<h1>This is the item page.</h1>")

def detail(request, item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item':item,
    }
    return render(request,'Food/detail.html',context)

def update_item(request,id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None,)
    
    if form.is_valid():
        form.save()
        return redirect("food:index")
    
    return render(request, 'food/item-form.html',{})

def create_item(request):
    form = ItemForm()
    context = {
        'form' = form
    }
    return redirect(request,'Food/item-form.html',context)

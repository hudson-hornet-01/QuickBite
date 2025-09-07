from django.urls import path
from . import views

app_name = 'Food'
urlpatterns = [
    # /food/
    path('',views.index,name='index'),
    # /food/1
    path('<int:item_id>/',views.detail,name='detail'),
    path('item/',views.item,name='item'),
    path('item/',views.item,name='item'),
    
]

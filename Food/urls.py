from django.urls import path
from . import views

app_name = 'Food'
urlpatterns = [
    # /food/
    path('',views.index,name='index'),
    # /food/1
    path('<int:id>/',views.detail,name='detail'),
    path('add/',views.create_item,name='create_item'),
    path('update/<int:id>/',views.update_item,name='update_item'),
]

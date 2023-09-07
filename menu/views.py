from django.shortcuts import render,get_object_or_404
from .models import Category,Menu

# Create your views here.
def menu(request):
    menus=Menu.objects.all()
    return render(request,"menu/menu.html",{'listMenus':menus})

def category(request,categoryId):
    #category= Category.objects.get(id=categoryId)
    category=get_object_or_404(Category,id=categoryId)
    menus=Menu.objects.filter(categories=category)
    return render(request,"menu/category.html",{'listMenus':menus})
from django.urls import path
from . import views
urlpatterns = [
    path('',views.menu,name='menu'),
    path('category/<int:categoryId>/',views.category,name="category")
]

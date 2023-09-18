from django.urls import path
from .views import adding_product, profile, shop_box, show_box, homes, vegas, car, jobs, animalss, other, search, home_pages

urlpatterns = [
    path('', home_pages, name='home'),
    path('profile/', profile, name='profile'),
    path('shopping/', shop_box, name='shop_box'),
    path('new/', adding_product, name='add'),
    path('show/<int:task_id>/', show_box, name='show'),
    path('vegas/', vegas, name='vegas'),
    path('home/', homes, name='house'),
    path('car/', car, name='car'),
    path('job/', jobs, name='job'),
    path('animals/', animalss, name='animals'),
    path('other/', other, name='other'),
    path('search/', search, name='search'),
]

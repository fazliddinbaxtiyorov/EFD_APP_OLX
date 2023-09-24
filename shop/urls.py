from django.urls import path
from .views import adding_product, profile, shop_box, show_box, homes, smart_watch, car, head, animalss, phone, search, home_pages
urlpatterns = [
    path('', home_pages, name='home'),
    path('profile/', profile, name='profile'),
    path('shopping/', shop_box, name='shop_box'),
    path('new/', adding_product, name='add'),
    path('show/<int:task_id>/', show_box, name='show'),
    path('watch/', smart_watch, name='watch'),
    path('home/', homes, name='house'),
    path('car/', car, name='car'),
    path('head_phone/', head, name='head'),
    path('animals/', animalss, name='animals'),
    path('phones/', phone, name='phone'),
    path('search/', search, name='search'),
]

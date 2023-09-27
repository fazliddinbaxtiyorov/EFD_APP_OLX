from django.urls import path
from .views import adding_product, profile, shop_box, show_box, homes, smart_watch, car, head, animalss, phone, search, home_pages, show_cars, show_animals, show_head, show_phone, show_watch, show_home
urlpatterns = [
    path('', home_pages, name='home'),
    path('profile/', profile, name='profile'),
    path('shopping/', shop_box, name='shop_box'),
    path('new/', adding_product, name='add'),
    path('show/<int:task_id>/', show_box, name='show'),
    path('show_head/<int:task_id>/', show_head, name='show_head'),
    path('show_home/<int:task_id>/', show_home, name='show_home'),
    path('show_watch/<int:task_id>/', show_watch, name='show_watch'),
    path('show_cars/<int:task_id>/', show_cars, name='show_cars'),
    path('show_phone/<int:task_id>/', show_phone, name='show_phone'),
    path('show_animals/<int:task_id>/', show_animals, name='show_animals'),
    path('watch/', smart_watch, name='watch'),
    path('home/', homes, name='house'),
    path('car/', car, name='car'),
    path('head_phone/', head, name='head'),
    path('animals/', animalss, name='animals'),
    path('phones/', phone, name='phone'),
    path('search/', search, name='search'),
]

from django.shortcuts import render, redirect, get_object_or_404

from users.forms import UserRegisterForm
from .forms import AddForm
from .models import AddModels, cars, home, head_phones, animals, phones, smart_watches
from django.db.models import Q


# Create your views here.
def adding_product(request):
    if request.method == 'POST':
        form = AddForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddForm()
    return render(request, 'shop/add.html', {'form': form})


def profile(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        username = form.cleaned_data.get('username')
        return render(request, 'shop/profile.html', {'user': username})
    else:
        form = UserRegisterForm()
        return render(request, 'shop/profile.html', {'form': form})


def shop_box(request):
    return render(request, 'shop/shopping.html')


def show_box(request, task_id):
    task = get_object_or_404(AddModels, id=task_id)
    if request.method == 'POST':
        return redirect('index')
    return render(request, 'shop/show.html', {'task': task})


def show_animals(request, task_id):
    task = get_object_or_404(animals, id=task_id)
    if request.method == 'POST':
        return redirect('index')
    return render(request, 'shop/show_animals.html', {'task': task})


def show_cars(request, task_id):
    task = get_object_or_404(cars, id=task_id)
    if request.method == 'POST':
        return redirect('index')
    return render(request, 'shop/show_cars.html', {'task': task})


def show_phone(request, task_id):
    task = get_object_or_404(phones, id=task_id)
    if request.method == 'POST':
        return redirect('index')
    return render(request, 'shop/show_phone.html', {'task': task})


def show_head(request, task_id):
    task = get_object_or_404(head_phones, id=task_id)
    if request.method == 'POST':
        return redirect('index')
    return render(request, 'shop/show_head.html', {'task': task})


def show_watch(request, task_id):
    task = get_object_or_404(smart_watches, id=task_id)
    if request.method == 'POST':
        return redirect('index')
    return render(request, 'shop/show_watch.html', {'task': task})


def show_home(request, task_id):
    task = get_object_or_404(home, id=task_id)
    if request.method == 'POST':
        return redirect('index')
    return render(request, 'shop/show_home.html', {'task': task})


def animalss(request):
    task = animals.objects.all()
    return render(request, 'shop/animals.html', {'task': task})


def smart_watch(request):
    task = smart_watches.objects.all()
    return render(request, 'shop/watch.html', {'task': task})


def car(request):
    task = cars.objects.all()
    return render(request, 'shop/car.html', {'task': task})


def head(request):
    task = head_phones.objects.all()
    return render(request, 'shop/head.html', {'task': task})


def homes(request):
    task = home.objects.all()
    return render(request, 'shop/home.html', {'task': task})


def phone(request):
    task = phones.objects.all()
    return render(request, 'shop/phone.html', {'task': task})


def home_pages(request):
    all_page_search = AddModels.objects.all()
    car_search = cars.objects.all()
    head_search = head_phones.objects.all()
    home_search = home.objects.all()
    animals_search = animals.objects.all()
    phone_search = phones.objects.all()
    smart_search = smart_watches.objects.all()
    return render(request, 'shop/index.html',
                  {'all_search': all_page_search, 'head_search': head_search, 'animals_search': animals_search,
                   'home_search': home_search, 'other_search': phone_search, 'vegas_search': smart_search,
                   'car_search': car_search})


def search(request):
    query = request.GET.get('q')
    all_page_search = AddModels.objects.filter(Q(title__icontains=query))
    car_search = cars.objects.filter(Q(title__icontains=query))
    head_search = head_phones.objects.filter(Q(title__icontains=query))
    home_search = home.objects.filter(Q(title__icontains=query))
    animals_search = animals.objects.filter(Q(title__icontains=query))
    phone_search = phones.objects.filter(Q(title__icontains=query))
    smart_search = smart_watches.objects.filter(Q(title__icontains=query))
    return render(request, 'shop/search.html', {'all_search': all_page_search, 'job_search': head_search, 'animals_search' : animals_search, 'home_search': home_search, 'other_search': phone_search, 'vegas_search': smart_search, 'car_search':car_search})

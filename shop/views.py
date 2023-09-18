from django.shortcuts import render, redirect, get_object_or_404
from .forms import AddForm
from .models import AddModels, cars, home, job, animals, others, vegas_all
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
    return render(request, 'shop/profile.html')


def shop_box(request):
    return render(request, 'shop/shopping.html')


def show_box(request, task_id):
    task = get_object_or_404(AddModels, id=task_id)
    if request.method == 'POST':
        return redirect('index')
    return render(request, 'shop/show.html', {'task': task})


def animalss(request):
    task = animals.objects.all()
    return render(request, 'shop/animals.html', {'task': task})


def vegas(request):
    task = vegas_all.objects.all()
    return render(request, 'shop/vegatables.html', {'task': task})


def car(request):
    task = cars.objects.all()
    return render(request, 'shop/car.html', {'task': task})


def jobs(request):
    task = job.objects.all()
    return render(request, 'shop/jobs.html', {'task': task})


def homes(request):
    task = home.objects.all()
    return render(request, 'shop/home.html', {'task': task})


def other(request):
    task = others.objects.all()
    return render(request, 'shop/others.html', {'task': task})


from django.contrib import admin
from .models import AddModels, cars, home, job, animals, others, vegas_all
# Register your models here.
admin.site.register(AddModels)
admin.site.register(cars)
admin.site.register(home)
admin.site.register(job)
admin.site.register(animals)
admin.site.register(others)
admin.site.register(vegas_all)

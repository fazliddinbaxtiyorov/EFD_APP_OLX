from django.contrib import admin
from .models import AddModels, cars, home, smart_watches, animals, phones, head_phones
# Register your models here.
admin.site.register(AddModels)
admin.site.register(cars)
admin.site.register(home)
admin.site.register(smart_watches)
admin.site.register(animals)
admin.site.register(head_phones)
admin.site.register(phones)

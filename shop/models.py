from django.db import models


class AddModels(models.Model):
    photo = models.ImageField(upload_to='media')
    title = models.CharField(max_length=70)
    date = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=150)
    categories = models.CharField(max_length=40, default='Enter categories')
    number = models.CharField(max_length=15, default='+9989')
    location = models.CharField(max_length=50)
    cost = models.CharField(max_length=15, default='0 $')


class cars(models.Model):
    title = models.CharField(max_length=70)
    number = models.CharField(max_length=15, default='+')
    description = models.CharField(max_length=150)
    location = models.CharField(max_length=50)
    cost = models.CharField(max_length=255)

    class Meta:
        db_table = 'cars'


class home(models.Model):
    title = models.CharField(max_length=70)
    number = models.CharField(max_length=15, default='+')
    description = models.CharField(max_length=150)
    location = models.CharField(max_length=50)
    cost = models.CharField(max_length=255)

    class Meta:
        db_table = 'home'


class job(models.Model):
    title = models.CharField(max_length=70)
    number = models.CharField(max_length=15, default='+')
    description = models.CharField(max_length=150)
    location = models.CharField(max_length=50)
    cost = models.CharField(max_length=255)

    class Meta:
        db_table = 'job'


class animals(models.Model):
    title = models.CharField(max_length=70)
    number = models.CharField(max_length=15, default='+')
    description = models.CharField(max_length=150)
    location = models.CharField(max_length=50)
    cost = models.CharField(max_length=255)

    class Meta:
        db_table = 'animals'


class others(models.Model):
    title = models.CharField(max_length=70)
    number = models.CharField(max_length=15, default='+')
    description = models.CharField(max_length=150)
    location = models.CharField(max_length=50)
    cost = models.CharField(max_length=255)

    class Meta:
        db_table = 'others'


class vegas_all(models.Model):
    title = models.CharField(max_length=70)
    number = models.CharField(max_length=15, default='+')
    description = models.CharField(max_length=150)
    location = models.CharField(max_length=50)
    cost = models.CharField(max_length=255)

    class Meta:
        db_table = 'vegas_all'

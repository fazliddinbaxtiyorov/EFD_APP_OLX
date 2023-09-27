# Generated by Django 4.2.5 on 2023-09-27 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='media')),
                ('title', models.CharField(max_length=70)),
                ('date', models.DateTimeField(auto_now=True)),
                ('description', models.CharField(max_length=150)),
                ('categories', models.CharField(default='Enter categories', max_length=40)),
                ('number', models.CharField(default='+9989', max_length=15)),
                ('location', models.CharField(max_length=50)),
                ('cost', models.CharField(default='0 $', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='animals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('number', models.CharField(default='+', max_length=15)),
                ('description', models.CharField(max_length=150)),
                ('location', models.CharField(max_length=50)),
                ('cost', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'animals',
            },
        ),
        migrations.CreateModel(
            name='cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('number', models.CharField(default='+', max_length=15)),
                ('description', models.CharField(max_length=150)),
                ('location', models.CharField(max_length=50)),
                ('cost', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'cars',
            },
        ),
        migrations.CreateModel(
            name='head_phones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('number', models.CharField(default='+', max_length=15)),
                ('description', models.CharField(max_length=150)),
                ('location', models.CharField(max_length=50)),
                ('cost', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'h_phone',
            },
        ),
        migrations.CreateModel(
            name='home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('number', models.CharField(default='+', max_length=15)),
                ('description', models.CharField(max_length=150)),
                ('location', models.CharField(max_length=50)),
                ('cost', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'home',
            },
        ),
        migrations.CreateModel(
            name='phones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('number', models.CharField(default='+', max_length=15)),
                ('description', models.CharField(max_length=150)),
                ('location', models.CharField(max_length=50)),
                ('cost', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'phone',
            },
        ),
        migrations.CreateModel(
            name='smart_watches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('number', models.CharField(default='+', max_length=15)),
                ('description', models.CharField(max_length=150)),
                ('location', models.CharField(max_length=50)),
                ('cost', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'watch',
            },
        ),
    ]

# Generated by Django 2.1.4 on 2019-02-01 06:21

import app.models
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('code', models.CharField(default='null', max_length=30, unique=True)),
                ('email', models.EmailField(max_length=30)),
                ('checkout_date', models.DateField(default=datetime.datetime.today)),
                ('due_date', models.DateField(default=app.models.deadline)),
                ('year', models.CharField(choices=[('2019', '2019'), ('2020', '2020'), ('2021', '2021'), ('2022', '2022')], max_length=4)),
            ],
        ),
    ]

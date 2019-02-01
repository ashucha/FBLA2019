from django.db import models, forms
from datetime import datetime, timedelta

def deadline():
    return datetime.today() + timedelta(days=30)

class Checkout(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    code = models.CharField(max_length=30, default='null', unique=True)
    email = models.EmailField(max_length=30)
    checkout_date = models.DateField(default=datetime.today)
    due_date = models.DateField(default=deadline)
    year = models.CharField(max_length=4, choices=[('2019', '2019'), ('2020', '2020'), ('2021', '2021'), ('2022', '2022')])

    def __str__(self):
        return str(self.id - 3 + 1000)


class Filter(forms.Form):
    query = forms.CharField(max_length=30)
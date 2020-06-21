from django.db import models

from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    email = models.EmailField(_('email address'), unique=True)  # changes email to unique and blank to false
    REQUIRED_FIELDS = []


class Category(models.Model):
    name = models.CharField(max_length=64)


fundacja = 'fundacja'
organizacja_pozarzadowa = 'organizacja_pozarządowa'
zbiorka_lokalna = 'zbiorka_lokalna'

TYPES_OF_INSTITUTIONS = (
    (fundacja, 'fundacja'),
    (organizacja_pozarzadowa, 'organizacja pozarządowa'),
    (zbiorka_lokalna, 'zbiórka lokalna'),
)


class Institution(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    type = models.CharField(choices=TYPES_OF_INSTITUTIONS, max_length=64, default=fundacja)
    categories = models.ManyToManyField(Category)


class Donation(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.CharField(max_length=64)
    phone_number = models.CharField(max_length=9)
    city = models.CharField(max_length=64)
    zip_code = models.CharField(max_length=6)
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    pick_up_comment = models.TextField()
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
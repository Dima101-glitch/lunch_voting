from django.contrib.auth.models import AbstractUser
from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Employee(AbstractUser):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, default=None, null=True)


class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="menus")
    date = models.DateField()
    items = models.JSONField()

    def __str__(self):
        return f"{self.restaurant.name} - {self.date}"

class Vote(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('employee', 'menu')


from django.db import models
from django.contrib.auth.models import User
from car.models import CarModel
# Create your models here.

class PurchaseModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='purchase')
    car = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name='purchase_by')
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} purchased {self.car.name}"
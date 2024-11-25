from django.db import models
from brand.models import BrandModel
# Create your models here.

class CarModel(models.Model):
    car_image = models.ImageField(upload_to='uploads/')
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(BrandModel, on_delete=models.CASCADE, related_name='cars')
    price = models.IntegerField()
    quantity = models.PositiveIntegerField(default=0, null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.name} {self.brand.Brand_Name}"

class CommentModel(models.Model):
    car = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    description = models.TextField()
    create_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.name}'


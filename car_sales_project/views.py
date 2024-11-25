from django.shortcuts import render
from car.models import CarModel
from brand.models import BrandModel

def home(request, brand_slug = None):
    data = CarModel.objects.all()
    if brand_slug is not None:
        category = BrandModel.objects.get(slug = brand_slug)
        data = CarModel.objects.filter(brand = category)
    brand_category = BrandModel.objects.all()
    return render(request, 'home.html', {'data' : data, 'brand_category' : brand_category})


from django.shortcuts import render
from django.views.generic import DetailView
from car.models import CarModel
from car.forms import CommentForm

# Create your views here.



class CarDetailViews(DetailView):
    model = CarModel
    template_name = 'car/car_details.html'
    pk_url_kwarg = 'id'
    
    def post(self, *args, **kwargs):
        comment_form = CommentForm(data = self.request.POST)
        car = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car = car
            new_comment.save()
        return self.get(self.request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.object
        brand = car.brand
        # brand_car_count = brand.cars.count()
        comments = car.comments.all()
        comment_form = CommentForm()
        
        context['car'] = car
        # context['brand_car_count'] = brand_car_count
        context['comments'] = comments
        context['comments_form'] = comment_form

        return context
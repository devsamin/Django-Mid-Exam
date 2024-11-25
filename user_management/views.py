from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth.models import User
from user_management.forms import UserRegisterForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from car.models import CarModel
from user_management.models import PurchaseModel
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from user_management.forms import ChangeUserForm
from django.views.generic.edit import UpdateView

class RegisterViews(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'user/register.html'
    success_url = reverse_lazy('registerpage')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        username = form.cleaned_data['username']
        user.save()
        messages.success(self.request, f'{username} Account Register successfully')
        return super().form_valid(form)



class Loginviews(LoginView):
    template_name = 'user/login.html'
    def get_success_url(self):
        return reverse_lazy('profilepage')
    
    def form_valid(self, form):
        username = form.cleaned_data['username']
        messages.success(self.request, f"{username} Login Successfully")
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.warning(self.request, "User information invalid")
        return super().form_invalid(form)

@login_required
def logoutviews(request):
    logout(request)
    return redirect('loginpage')

@login_required
def profileviews(request):
    purchases = PurchaseModel.objects.filter(user = request.user)
    return render(request, 'user/profile.html', {'purchases' : purchases})

@login_required
def BuyCarviews(request, id):
    car = CarModel.objects.get(pk = id)
    if car.quantity > 0:
        car.quantity-= 1
        car.save()
        PurchaseModel.objects.create(user = request.user, car = car)
        messages.success(request,f'{car.name} successfully purchased. Remaning stock : {car.quantity}')
    else:
        messages.warning(request, f'Sorry, {car.name} is out of stock!')
    return redirect('profilepage')

# def EditProfileviews(request):
#     if request.method == 'POST':
#         Profile_form = ChangeUserForm(request.POST, instance = request.user)
#         if Profile_form.is_valid():
#             messages.success(request, 'User profile update successfully.')
#             Profile_form.save()
#             return redirect('profilepage')
#     else:
#         Profile_form = ChangeUserForm(instance = request.user)
#     return render(request, 'user/edit_profile.html', {'form' : Profile_form})

class UpdateProfileViews(UpdateView):
    model = User
    form_class = ChangeUserForm
    template_name = 'user/edit_profile.html'
    success_url = reverse_lazy('profilepage')
    def get_object(self):
        return self.request.user
    def form_valid(self, form):
        messages.success(self.request, 'User profile update successfully.')
        return super().form_valid(form)

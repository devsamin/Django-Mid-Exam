
from django.urls import path
from user_management.views import RegisterViews, Loginviews, logoutviews, profileviews, BuyCarviews, UpdateProfileViews

urlpatterns = [
    path('register/', RegisterViews.as_view(), name='registerpage'),
    path('login/', Loginviews.as_view(), name='loginpage'),
    path('logout/', logoutviews, name='logoutpage'),
    path('profile/', profileviews, name='profilepage'),
    path('buycar/<int:id>/', BuyCarviews, name='BuyCarpage'),
    path('edit_profile/', UpdateProfileViews.as_view(), name='editprofile'),

]
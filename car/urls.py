from django.contrib import admin
from django.urls import path
from car import views
urlpatterns = [
    path('car_details/<int:id>/', views.CarDetailViews.as_view(), name="car_details"),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.car_form, name='car_form'),  # Main form
    path('result/', views.result, name='result'),  # Result page
]

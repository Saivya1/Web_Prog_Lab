from django.urls import path
from . import views

urlpatterns = [
    path('firstPage/', views.first_page, name='first_page'),
    path('secondPage/', views.second_page, name='second_page'),
    path('', views.first_page, name='first_page_redirect'),  # Redirect to first page on '/' path
]

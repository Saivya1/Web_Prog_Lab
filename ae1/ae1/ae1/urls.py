from django.contrib import admin
from django.urls import path
from webapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page, name='home_page'),
    path('metadata/', views.metadata_page, name='metadata_page'),
    path('reviews/', views.reviews_page, name='reviews_page'),
    path('publisher/', views.publisher_page, name='publisher_page'),
]

from django.urls import path

from . import views

urlpatterns = [
    path('book/', views.newBook, name='book'),
    path('all/', views.newBook, name='all'),
    path('car/', views.newCar, name='car'),
    path('all/', views.newCar, name='all'),
]
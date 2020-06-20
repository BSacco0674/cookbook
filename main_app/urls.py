from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recipes/', views.recipes, name='recipies'),
    path('search/', views.search, name='search'),
    path('profile/', views.profile, name='profile'),
]
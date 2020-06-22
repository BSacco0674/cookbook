from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recipes/', views.recipes, name='recipies'),
    path('results/', views.search_results, name='search_results'),
    path('profile/', views.profile, name='profile'),
    path('detail/', views.detail, name='detail'),
    path('accounts/signup/', views.signup, name='signup'),
]
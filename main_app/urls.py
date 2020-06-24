from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recipes/', views.recipes_index, name='recipes_index'),
    path('results/', views.search_results, name='search_results'),
    path('profile/', views.profile, name='profile'),
    path('recipes/<int:recipe_id>/', views.recipe_detail, name='detail'),
    path('accounts/signup/', views.signup, name='signup'),
    path('recipes/create/', views.RecipeCreate.as_view(), name='recipe_create'),
    path('recipes/<int:pk>/update/', views.RecipeUpdate.as_view(), name='recipe_update'),
    path('recipes/<int:pk>/delete/', views.RecipeDelete.as_view(), name='recipe_delete'),
]
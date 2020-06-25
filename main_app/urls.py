from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('recipes/', views.recipes_index, name='recipes_index'),
    path('recipes/create/', views.RecipeCreate.as_view(), name='recipe_create'),
    path('recipes/<int:recipe_id>/', views.recipe_detail, name='detail'),
    path('recipes/<int:pk>/update/', views.RecipeUpdate.as_view(), name='recipe_update'),
    path('recipes/<int:pk>/delete/', views.RecipeDelete.as_view(), name='recipe_delete'),
    path('recipes/<int:recipe_id>/add_review/', views.add_review, name='add_review'),
    path('recipes/<int:recipe_id>/add_modification/', views.add_modification, name='add_modification'),
]
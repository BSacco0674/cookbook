from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Recipe, Review

# Create your views here.
def home(request):
    return render(request, 'home.html')

def recipes_index(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/index.html', {'recipes': recipes})

def recipe_detail(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    return render(request, 'recipes/detail.html', { 'recipe': recipe })

def search_results(request):
    return render(request, 'results.html')

def profile(request):
    return render(request, 'profile.html')

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else :
            error_message = 'Invalid sign-up, please try again.'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message }
    return render(request, 'registration/signup.html', context)


class RecipeCreate(CreateView):
  model = Recipe
  fields = '__all__'

class RecipeUpdate(UpdateView):
  model = Recipe
  fields = '__all__'

class RecipeDelete(DeleteView):
  model = Recipe
  success_url = '/recipes/'

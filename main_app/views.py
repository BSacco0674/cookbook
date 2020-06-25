from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Recipe, Review, User
from .forms import ReviewForm, ModificationForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def recipes_index(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/index.html', {'recipes': recipes})

def recipe_detail(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    items = recipe.ingredients.split(',')
    steps = recipe.instructions.split('.')
    steps.pop()
    review_form = ReviewForm()
    modification_form = ModificationForm()
    return render(request, 'recipes/detail.html', { 
        'recipe': recipe, 
        'items': items, 
        'steps': steps, 
        'review_form': review_form, 
        'modification_form': modification_form })

def search_results(request):
    return render(request, 'results.html')

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('recipes_index')
        else :
            error_message = 'Invalid sign-up, please try again.'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message }
    return render(request, 'registration/signup.html', context)

# class RecipeCreate(CreateView):
#   model = Recipe
#   fields = '__all__'

class RecipeCreate(LoginRequiredMixin, CreateView):
  model = Recipe
  fields = ['name', 'ingredients', 'instructions']

  def form_valid(self, form):
    # Assign the logged in user
    form.instance.user = self.request.user
    # Let the CreateView do its job as usual
    return super().form_valid(form)


class RecipeUpdate(LoginRequiredMixin, UpdateView):
  model = Recipe
  fields = '__all__'


class RecipeDelete(LoginRequiredMixin, DeleteView):
  model = Recipe
  success_url = '/recipes/'

# @login_required
def add_review(request, recipe_id):
  form = ReviewForm(request.POST)
  if form.is_valid():
    new_review = form.save(commit=False)
    new_review.recipe_id = recipe_id
    new_review.save()
  return redirect('detail', recipe_id=recipe_id)

# @login_required
def add_modification(request, recipe_id):
  form = ModificationForm(request.POST)
  if form.is_valid():
    new_modification = form.save(commit=False)
    new_modification.recipe_id = recipe_id
    new_modification.save()
  return redirect('detail', recipe_id=recipe_id)
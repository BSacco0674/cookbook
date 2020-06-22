from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request):
  return render(request, 'home.html')

def recipes(request):
    return render(request, 'recipes/index.html')

def search_results(request):
    return render(request, 'results.html')

def profile(request):
    return render(request, 'profile.html')

def detail(request):
    return render(request, 'recipes/detail.html')

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
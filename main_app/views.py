from django.shortcuts import render


# Create your views here.
def home(request):
  return render(request, 'home.html')

def recipes(request):
    return render(request, 'recipes.html')

def search(request):
    return render(request, 'search.html')

def profile(request):
    return render(request, 'profile.html')
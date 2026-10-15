from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout

# Create your views here.
def index(request):
    return HttpResponse("Authentication")

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if  form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()

        return render(request, 'register.html', {'form':form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home') # Redirect to homepage
    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect('home')

def user_home(request):
    return render(request, 'home.html')

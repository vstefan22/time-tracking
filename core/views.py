from django.shortcuts import render, redirect
# Authentication imports
from django.contrib.auth import login, authenticate 
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm 
from .forms import RegisterForm

# Models
from .models import Project, Notification, Role, Tasks

def index(request):
    return render(request, 'core/index.html')

# Authentication functions start
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password =  request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('core:index')

    form = AuthenticationForm()
    context={"login_form":form}
    return render(request, 'core/login.html', context)


def logout_request(request):
    logout(request)
    return redirect('core:login')


def register_request(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)   
        if form.is_valid():
            user = form.save()
            login(request, user)
        return redirect("/")
    else:
        form = RegisterForm()

    return render(request, "core/register.html", {"form":form})

# Authentication functions end
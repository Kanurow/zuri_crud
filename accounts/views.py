from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='login')
def home(request):
    return render(request, 'accounts/dashboard.html')

@login_required(login_url='login')
def products(request):
    return render(request, 'accounts/products.html')

@login_required(login_url='login')
def customer(request):
    return render(request, 'accounts/customer.html')

def registerPage(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            new_user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for '+ new_user)

        return redirect('login')
    context = {'form':form}
    return render(request, "accounts/register.html", context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'username or password is incorrect')
            return render(request, "accounts/login.html")
    return render(request, "accounts/login.html")



def logout_user(request):
    logout(request)
    return redirect('login')


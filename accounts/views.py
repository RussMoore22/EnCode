from django.shortcuts import render
from .forms import LoginForm, Signup_Form
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect
from django.contrib.auth.models import User
#from django.contrib.auth.models import User

# Create your views here.


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():

            un = form.cleaned_data['username']
            pw = form.cleaned_data['password']
            user = authenticate(request, username=un, password=pw)
            if user is not None:
                login(request, user)
                return redirect('inbox_list')

    else:
        form = LoginForm()
    context = {
            "form": form
    }
    return render(request, "accounts/login.html", context)

def user_logout(request):
    logout(request)
    return redirect('login')


# user signup:

def user_signup(request):
    if request.method == "POST":
        form = Signup_Form(request.POST)

        if form.is_valid():
            un = form.cleaned_data['username']
            pw = form.cleaned_data['password']
            pwc = form.cleaned_data['password_confirmation']
            if pw == pwc:
                user = User.objects.create_user(un, email=None, password=pw)
                if user is not None:
                    login(request, user)
                    return redirect('inbox_list')
            else:
                form.add_error("password_confirmation", "the passwords do not match")

    elif request.method == "GET":
        form = Signup_Form()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)

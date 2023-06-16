from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def HomePage(request):
    return render(request, 'auth_system/index.html', {})

def Register(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('sname')
        name = request.POST.get('uname')
        email = request.POST.get('email')
        password = request.POST.get('pass')

        new_user = User.objects.create_user(name, email, password)
        new_user.first_name = fname
        new_user.last_name = lname

        new_user.save()
        return redirect('login-page')

    return render(request, 'auth_system/register.html', {})

def Login(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        password = request.POST.get('pass')

        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request, user)
            return redirect('home-page')
        else:
            return HttpResponse('Error, user does not exist')


    return render(request, 'auth_system/login.html', {})


def main_page(request):
    return render(request, 'index.html', {})

def main_page_pl(request):
    return render(request, 'index2.html', {})

def programs(request):
    return render(request, 'Programs.html', {})

def programs_pl(request):
    return render(request, 'ProgramsPL.html', {})

def py(request):
    return render(request, 'PY.html', {})

def py_pl(request):
    return render(request, 'PYPL.html', {})

def info(request):
    return render(request, 'Info.html', {})

def info_pl(request):
    return render(request, 'InfoPL.html', {})

def other(request):
    return render(request, 'Other.html', {})

def other_pl(request):
    return render(request, 'OtherPL.html', {})

def logoutuser(request):
    logout(request)
    return redirect('login-page')


from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, NewUserForm
from django.contrib import messages
from .models import UserInfo, UserRequests, ClearPrice


def index(requests):
    return render(requests, 'service/base.html', {})


def how_it_work(requests):
    return render(requests, 'service/how_it_work.html', {})


def price_list(requests):
    return render(requests, 'service/price_list.html', {})


def contacts(requests):
    return render(requests, 'service/contacts.html')


def cabinet(request, user_id):
    if request.user.is_authenticated:
        user_info = UserInfo.objects.filter(user=request.user)
        user_request = UserRequests.objects.filter(user=request.user)
        clear_price = ClearPrice.objects.all()
        for elem in clear_price:
            clear_price = elem.clear_price
        for elem in user_info:
            balance = elem.balance/clear_price
        return render(request, 'service/cabinet.html', {'user_info': round(int(balance), 1), 'user_request': user_request})
    else:
        return redirect('login')


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            print(user)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(f'cabinet/{user}')
                else:
                    return render(request, 'service/login.html', {'form': form})
            else:
                return render(request, 'service/login.html', {'form': form})
    else:
        form = LoginForm()
    return render(request, 'service/login.html', {'form': form})


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect(user_login)
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request, "service/register.html", {"register_form": form})


def user_logout(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("homepage")
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages, auth
from django.urls import reverse
from api.models import Menu, Vote
from django.utils.timezone import now

from interface.forms import ProfileForm, LoginForm, RegisterForm

@login_required
def menus(request):
    context = {
        'all_menus': Menu.objects.filter(restaurant=request.user.restaurant, date=now().date()),
    }
    return render(request, 'menus.html', context)


def make_vote(request, menu_id):
    vote = Vote.objects.filter(employee=request.user, menu_id=menu_id)
    if not vote.exists():
        vote_make = Vote.objects.filter(employee=request.user, menu__date=now().date())
        if vote_make.exists():
            vote_make.delete()
        Vote.objects.create(employee=request.user, menu=Menu.objects.get(id=menu_id))
    else:
        messages.error(request, 'You have already voted!')
        return HttpResponseRedirect(reverse('interface:messages_info'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def messages_info(request):
    return render(request, 'messages.html')


@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(instance=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return HttpResponseRedirect(reverse('interface:messages_info'))
    else:
        form = ProfileForm(instance=request.user)

    context = {
        'form': form,
    }
    return render(request, 'profile.html', context)


def login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(request, username=username, password=password)
            if user:
                auth.login(request, user)
                messages.success(request, 'You have successfully logged in!')
                return HttpResponseRedirect(reverse('interface:messages_info'))
    else:
        form = LoginForm()

    context = {
        'form': form,
    }
    return render(request, 'login.html', context)


@login_required
def logout(request):
    auth.logout(request)
    messages.info(request, 'You was logged out!')
    return HttpResponseRedirect(reverse('interface:messages_info'))


def register(request):
    if request.method == "POST":
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully!")
            messages.success(request, "Try to login with your data now!")
            return HttpResponseRedirect(reverse('interface:login'))
    else:
        form = RegisterForm()

    context = {
        "form": form
    }
    return render(request, 'register.html', context)

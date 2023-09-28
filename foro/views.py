from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from foro.models import Thread


# Create your views here.
def thread_list(request):
    return render(request, 'foro/index.html', {'threads': Thread.objects.all()})


def add_thread(request):
    return render(request, 'foro/add.html')


@login_required  # Use the login_required decorator to ensure the user is logged in.
def add_thread_post(request):
    title = request.POST['title']
    content = request.POST['content']
    author = request.user.username  # Set the author as the username of the logged-in user

    thread = Thread(title=title, author=author, content=content)
    thread.save()
    return HttpResponseRedirect(reverse('thread_list'))


def login_view(request):
    return render(request, 'foro/login.html')


def signup(request):
    return render(request, 'foro/signup.html')


def kontua_sortu(request):
    # Create an account
    username = request.POST['username']
    password = request.POST['password']
    password2 = request.POST['password2']
    if password == password2:
        user = User.objects.create_user(username, password)
        user.set_password(password)
        user.save()
        return HttpResponseRedirect(reverse('thread_list'))
    else:
        return HttpResponseRedirect(reverse('signup'))


def auth(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Log the user in
            user = form.get_user()
            login(request, user)  # Pass the request and user to login
            return HttpResponseRedirect(reverse('thread_list'))
    else:
        form = AuthenticationForm()

    return render(request, 'foro/login.html', {'form': form})
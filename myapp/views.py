from django.shortcuts import render, redirect
from forms import SignUpForm
from models import UserModel
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password

# Create your views here.


def signup_view(request):
  if request.method == "POST":
    form = SignUpForm(request.POST)
    if form.is_valid():
      username = form.cleaned_data['username']
      name = form.cleaned_data['name']
      email = form.cleaned_data['email']
      password = form.cleaned_data['password']
  elif request.method == "GET":
    form = SignUpForm()

  return render(request, 'index.html', {'form' : form})
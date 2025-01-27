from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login , logout as auth_logout, authenticate


def home(request):
    return render(request, 'accounts/home.html')


def user_login(request):
    if request.method == "POST":
        email = request.POST.get('email').strip()
        password = request.POST.get('password')

        
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, "User does not exist. Please register first.")
            return redirect("/accounts/register/")
        
        user = authenticate(username=user.username, password=password)
        if user is None:
            messages.error(request, "Invalid username or password.")
            return redirect('/accounts/login/')
        
        if not user.is_active:
            messages.error(request, "This account is inactive.")
            return redirect('/accounts/login/')
        
        login(request, user)
        return redirect('/accounts/') 
    
    return render(request, 'accounts/login.html')


def register(request):
    if request.method == "POST":
        username = request.POST.get('username').strip()
        email = request.POST.get('email').strip()
        password = request.POST.get('password')
        vpassword = request.POST.get('vpassword')

        errors = []

        if not username:
            errors.append("Username is required.")
        if not email:
            errors.append("Email is required.")
        if not password or not vpassword:
            errors.append("Password and Confirm Password are required.")
        if password != vpassword:
            errors.append("Passwords do not match.")
        if User.objects.filter(email=email).exists():
            errors.append("Email already exists! Please register with a different email.")
        if User.objects.filter(username=username).exists():
            errors.append("Username already exists! Please choose another.")

        if errors:
            return render(request, 'accounts/register.html', {
                'errors': errors,
                'username': username,
                'email': email,
            })

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        messages.success(request, 'Registration successful! Please log in.')
        return redirect('/accounts/login/')

    return render(request, 'accounts/register.html')


def user_logout(request):
    auth_logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('/accounts/login/')

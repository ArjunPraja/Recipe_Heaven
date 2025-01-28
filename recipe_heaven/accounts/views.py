from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login , logout as auth_logout, authenticate
from .models import user_image
from racipies.models import Recipes

def home(request):
    return render(request, 'accounts/home.html')

def user_upload_images(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        if image:
            # Save the uploaded image and associate it with the logged-in user
            user_image.objects.create(user=request.user, user_image=image)
            return redirect('profile')  # Redirect to the user profile page or any desired URL
        else:
            return redirect('profile')
    return render(request, 'accounts/user_profile.html')
def user_profile(request):
    user = get_object_or_404(User, id=request.user.id)
    print(request.user)
    image=user_image.objects.filter(user=request.user)
    recipies=Recipes.objects.filter(user=request.user)
    return render(request,'accounts/user_profile.html',{'user':user, 'image':image,'recipies':recipies})

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

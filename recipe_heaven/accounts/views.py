from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login , logout as auth_logout, authenticate
from .models import user_image
from racipies.models import Recipes, Rating, Favourite
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse









def user_profile_image(request):
    if request.user.is_authenticated:
        try:
            user_profile = user_image.objects.get(user=request.user)
            return {'profile_image_url': user_profile.profile_image.url}
        except user_image.DoesNotExist:
            # Default image if no profile exists
            return {'profile_image_url':None}
    return {'profile_image_url': None}


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





@login_required(login_url='accounts/login') 
def user_profile(request):
    user = get_object_or_404(User, id=request.user.id)
    print(request.user)
    image=user_image.objects.filter(user=request.user)
    recipies=Recipes.objects.filter(user=request.user)
    review=Rating.objects.filter(user=request.user)
    user_favorite_recipes = Favourite.objects.filter(user=request.user)
    return render(request,'accounts/user_profile.html',{'user':user, 'image':image,'recipies':recipies,'review':review, 'favorite_recipes': user_favorite_recipes})

def user_login(request):
    if request.method == "POST":
        email = request.POST.get('email').strip()
        password = request.POST.get('password')

        
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.warning(request, "User does not exist. Please register first.")
            return redirect("/accounts/login/")
        
        user = authenticate(username=user.username, password=password)
        if user is None:
            messages.warning(request, "Invalid username or password.")
            return redirect('/accounts/login/')
        
        if not user.is_active:
            messages.warning(request, "This account is inactive.")
            return redirect('/accounts/login/')
        
        login(request, user)
        return redirect('/accounts/') 
    
    return render(request, 'accounts/login.html')

from django.contrib import messages

def register(request):
    if request.method == "POST":
        username = request.POST.get('username').strip()
        email = request.POST.get('email').strip()
        password = request.POST.get('password')
        vpassword = request.POST.get('vpassword')

        if not username or not email or not password or not vpassword:
            messages.warning(request, "All fields are required.")
            redirect('accounts/login/')
        elif password != vpassword:
            messages.warning(request, "Passwords do not match.")
            redirect('accounts/login/')

        elif User.objects.filter(email=email).exists():
            messages.warning(request, "Email already exists! Please register with a different email.")
            redirect('accounts/login/')

        elif User.objects.filter(username=username).exists():
            messages.warning(request, "Username already exists! Please choose another.")
            redirect('accounts/login/')

        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, 'Registration successful! Please log in.')
            return redirect('/accounts/login/')
        
    return render(request, 'accounts/register.html')

@login_required(login_url='accounts/login') 
def user_logout(request):
    auth_logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('/accounts/login/')





@login_required
def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipes, id=recipe_id)
    
    if request.method == "POST":
        if request.user == recipe.user:
            recipe.delete()
            messages.success(request, "Recipe deleted successfully.")
        else:
            messages.error(request, "You are not authorized to delete this recipe.")
    else:
        messages.warning(request, "Invalid request method.")

    return redirect('/accounts/profile/')  # Redirect to the profile page or another suitable page

@login_required
def delete_rating(request, rating_id):
    rating = get_object_or_404(Rating, id=rating_id)
    if request.user==rating.user:
        rating.delete()
        messages.success(request, "Rating deleted successfully.")
    else:
        messages.error(request, "You are not authorized to delete this rating.")
    return redirect('/accounts/profile/')  # Absolute URL




def remove_favourite(request,favorite_id):
    Favourite.objects.filter(id=favorite_id).delete()
    messages.success(request,"Recipies Remove From The Favourite SuccessFully ")
    return redirect('/accounts/profile/')





def custom_404(request, exception):
    """
    Custom 404 Error Handler - Redirects users to the homepage
    when they access an invalid URL.
    """
    return redirect('home')
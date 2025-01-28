from django.shortcuts import render, HttpResponse, redirect
from .models import Recipes
from django.contrib import messages
# Create your views here.

def recipies(request):
    if request.method=="GET":
        data=Recipes.objects.all()
        return render(request,"racipies/recipies.html",{'data':data})
    return render(request,"racipies/recipies.html")

def add_recipies(request):
    if request.method=='POST':
        recipe_name=request.POST.get('recipe_name')
        recipe_category=request.POST.get('recipe_category')
        prep_time=request.POST.get('prep_time')
        cook_time=request.POST.get('cook_time')
        description=request.POST.get('description')
        image=request.FILES.get('image')

        Recipes.objects.create(
            recipe_name=recipe_name,
            recipe_category=recipe_category,
            prep_time=prep_time,
            cook_time=cook_time,
            description=description,
            image=image if image else None,
            user=request.user
        )
        messages.success(request,message="Recipies Added Successfully")
        return redirect('/recipies/add/')
    return render(request,"racipies/add_recipies.html")
from django.shortcuts import render, HttpResponse, redirect,  get_object_or_404
from .models import Recipes, Rating, Favourite
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

@login_required(login_url='/accounts/login/')
def recipies(request):
    if request.method == "GET":
        data = Recipes.objects.all()
        
        for item in data:
            item.reviews = Rating.objects.filter(recipe=item)  
        return render(request, "racipies/recipies.html", {'data': data})
    return render(request, "racipies/recipies.html")


@login_required(login_url='/accounts/login/')
def add_recipies(request):
    if request.method=='POST':
        recipe_name=request.POST.get('recipe_name')
        recipe_category=request.POST.get('recipe_category')
        prep_time=request.POST.get('prep_time')
        cook_time=request.POST.get('cook_time')
        description=request.POST.get('description')
        ingredients=request.POST.get('ingredients')
        steps=request.POST.get('steps')
        image=request.FILES.get('image')
        if not recipe_name or not recipe_category or not prep_time or not cook_time or not description or not ingredients or not steps or not image:
            print("Please make sure all fields are filled.")
            return redirect('/recipies/add/')
        Recipes.objects.create(
            recipe_name=recipe_name,
            recipe_category=recipe_category,
            prep_time=prep_time,
            cook_time=cook_time,
            description=description,
            steps=steps,
            ingredients=ingredients,
            image=image if image else None,
            user=request.user
        )
        messages.success(request,message="Recipies Added Successfully")
        return redirect('/recipies/add/')
    
    return render(request,"racipies/add_recipies.html")




@login_required(login_url='/accounts/login/')
def submit_review(request, recipe_id):
    recipe = get_object_or_404(Recipes, id=recipe_id)
    
    if request.method == "POST":
        rating_value = request.POST.get("rating")
        review_text = request.POST.get("reviewText")
        

        Rating.objects.create(
            recipe=recipe,
            user=request.user,
            rating=rating_value,
            review=review_text
        )
        messages.success(request,"Review Submitted Successfully")
        return redirect('recipies')  

    return redirect('recipies') 



@login_required
def toggle_favourite(request, id):
    recipe = get_object_or_404(Recipes, id=id)

    favourite = Favourite.objects.filter(user=request.user, recipe=recipe).first()

    if favourite:
        favourite.delete()
        messages.success(request,"Recipes SuccessFully Deleted To The Favourite ")
        is_favorite = False
    else:
        Favourite.objects.create(user=request.user, recipe=recipe)
        messages.success(request,"Recipes SuccessFully Added To The Favourite ")

        is_favorite = True

    return JsonResponse({'is_favorite': is_favorite})




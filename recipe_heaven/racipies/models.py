from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Recipes(models.Model):
    
    recipe_name = models.CharField(max_length=150)
    recipe_category = models.CharField(max_length=100)
    prep_time = models.PositiveIntegerField(help_text="Preparation time in minutes")
    cook_time = models.PositiveIntegerField(help_text="Cooking time in minutes")
    description = models.TextField(blank=True, help_text="Brief description of the recipe")
    ingredients=models.TextField(blank=True)
    steps=models.TextField(blank=True)
    image = models.ImageField(upload_to='recipes/', blank=True, null=True, help_text="Upload an image of the recipe")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes', null=True)
  # Add user field

    def __str__(self):
        return self.recipe_name

    def total_time(self):
        return self.prep_time + self.cook_time

    def average_rating(self):
        ratings = self.ratings.all()
        if ratings.exists():
            return round(sum(rating.rating for rating in ratings) / ratings.count(), 2)
        return 0

    def total_ratings(self):
        return self.ratings.count()



class Rating(models.Model):
    recipe = models.ForeignKey(
        Recipes, on_delete=models.CASCADE, related_name="ratings"
    )
    user = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, null=True, blank=True, related_name="user_ratings"
    )
    rating = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5),
        ],
        help_text="Rating value between 1 (worst) and 5 (best)",
    )
    review = models.TextField(blank=True, null=True, help_text="Write a review for this recipe")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Rating: {self.rating} for Recipe: {self.recipe.recipe_name}"
    



# In models.py
class Favourite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.recipe.recipe_name}"
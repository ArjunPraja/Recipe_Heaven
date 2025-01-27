
# Register your models here.
from django.contrib import admin
from .models import Recipes, Rating

@admin.register(Recipes)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ("recipe_name", "recipe_category", "prep_time", "cook_time", "average_rating", "total_ratings", "updated_at")
    search_fields = ("recipe_name", "recipe_category")
    list_filter = ("recipe_category", "created_at", "updated_at")


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ("recipe", "user", "rating", "created_at")
    search_fields = ("recipe__recipe_name", "user__username")
    list_filter = ("rating", "created_at")

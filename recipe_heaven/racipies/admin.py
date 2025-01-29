
# Register your models here.
from django.contrib import admin
from .models import Recipes, Rating, Favourite

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



class FavouriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe')  # Add 'created_at' if your model has it these fields
    list_filter = ('user', 'recipe')
    search_fields = ('user__username', 'recipe__recipe_name')
    raw_id_fields = ('user', 'recipe')

    def __str__(self):
        return f"{self.user.username} - {self.recipe.recipe_name}"
    
admin.site.register(Favourite, FavouriteAdmin)


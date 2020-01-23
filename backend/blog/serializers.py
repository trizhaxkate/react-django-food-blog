from rest_framework import serializers
from .models import Recipe, Procedure, Users

class RecipeSerializer(serializers.ModelSerializer):
    procedures = serializers.StringRelatedField(many=True)
    # category = serializers.StringRelatedField(many=True)
    recipe_category = serializers.CharField(source='recipe_category.category_title')
    # recipe_author = serializers.CharField(source='recipe_author.username')
    class Meta:
        model = Recipe
        fields = ('id', 'recipe_title', 'recipe_author', 'recipe_category', 'recipe_ingredient', 'recipe_image', 'procedures', 'recipe_description', 'recipe_timestamp', 'recipe_duration', 'recipe_serving')
        
class ProcedureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Procedure
        fields = ('instruction', 'recipe_id')
        
# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = ('category_title')

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = (
            'id',
            'is_staff',
            'username',
            'password',
            'email',
            'first_name',
            'last_name',
            'contact_number',
            'avatar',
        )
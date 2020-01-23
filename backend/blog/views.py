from django.shortcuts import render
from rest_framework import viewsets          # add this
from .serializers import RecipeSerializer, ProcedureSerializer, UsersSerializer     # add this
from .models import Recipe, Procedure, Users               # add this

class RecipeView(viewsets.ModelViewSet):       # add this
    serializer_class = RecipeSerializer          # add this
    queryset = Recipe.objects.all()              # add this
    
class ProcedureView(viewsets.ModelViewSet):       # add this
    serializer_class = ProcedureSerializer          # add this
    queryset = Procedure.objects.all()              # add this
    
class UsersView(viewsets.ModelViewSet):
    serializer_class = UsersSerializer
    queryset = Users.objects.all()
    
# class CategoryView(viewsets.ModelViewSet):       # add this
#     serializer_class = CategorySerializer          # add this
#     queryset = Category.objects.all() 
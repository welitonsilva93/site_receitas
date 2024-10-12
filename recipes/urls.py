from django.urls import path
from recipes.views import contato, sobre, home

urlpatterns = [
    path('', home),
    path('contato/', contato),
    path('sobre/', sobre),
]
from django.urls import path
from .views import home, categoria, registro

urlpatterns = [
    path('', home, name="home"),
    path('categorias/',categoria, name ='categoria'),
    path('registro/',registro, name ='registro'),
]

from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('products/',views.list_products,name='list_products'),
    path('products/<int:id>/', views.products_item, name='products_item'),
    path('categories/', views.list_categories, name='list_categories'),
    path('categories/<int:id>/',views.categories_item, name='categories_item'),

]
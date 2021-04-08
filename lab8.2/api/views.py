from django.shortcuts import render
from api.models import Product
from api.models import Category
from django.http.response import JsonResponse

def list_products(request):
    products=Product.objects.all()
    products_json=[product.to_json() for product in products]
    return JsonResponse(products_json,safe=False)

def products_item(request,id):
    try:
        products = Product.objects.get(id=id)
    except Product.DoesNotExist as e:
        return JsonResponse({'message':str(e)},status=400)
    return JsonResponse(products.to_json())

def list_categories(request):
    categories = Category.objects.all()
    categories_json = [item.to_json() for item in categories]
    return JsonResponse(categories_json, safe=False)

def categories_item(request,id):
    try:
        categories= Category.objects.get(id=id)
    except Category.DoesNotExist as e:
        return JsonResponse({'message':str(e)},status=400)
    return JsonResponse(categories.to_json())


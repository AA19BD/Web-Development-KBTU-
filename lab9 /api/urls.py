from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('companies/', views.list_companies, name='list_companies'),
    path('companies/<int:id>/', views.companies_item, name='companies_item'),
    path('companies/<int:id>/vacancies/', views.list_of_vacancies_by_company,name='list_of_vacancies_by_company'),
    path('vacancies/', views.list_vacancies, name='list_vacancies'),
    path('vacancies/<int:id>/', views.vacancies_item, name='vacancies_item'),
    path('vacancies/top_ten/', views.top_ten, name='top_ten'),
]

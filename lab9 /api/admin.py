from django.contrib import admin
from api.models import Company, Vacancy


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'salary', 'company')
    search_fields = ('name', 'salary', 'company')
    list_filter = ('company',)


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'city', 'address')

# Register your models here.

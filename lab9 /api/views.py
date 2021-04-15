from django.shortcuts import render
from api.models import Company, Vacancy
from django.http.response import JsonResponse


def list_companies(request):
    companies = Company.objects.all()
    companies_json = [item.to_json() for item in companies]
    return JsonResponse(companies_json, safe=False)


def companies_item(request, id):
    try:
        companies = Company.objects.get(id=id)
    except Company.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)
    return JsonResponse(companies.to_json())


def list_of_vacancies_by_company(request, id):
    try:
        companies = Company.objects.get(id=id)
    except Company.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)
    call=companies.vacancy_set.all()
    call_json = [item.to_json() for item in call]
    return JsonResponse(call_json, safe=False)


def list_vacancies(request):
    vacancies = Vacancy.objects.all()
    vacancies_json = [item.to_json() for item in vacancies]
    return JsonResponse(vacancies_json, safe=False)


def vacancies_item(request, id):
    try:
        vacancies = Vacancy.objects.get(id=id)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)
    return JsonResponse(vacancies.to_json())


def top_ten(request):
    vacancies = Vacancy.objects.all().order_by("-salary")[:10]
    vacancies_json = [item.to_json() for item in vacancies]
    return JsonResponse(vacancies_json, safe=False)

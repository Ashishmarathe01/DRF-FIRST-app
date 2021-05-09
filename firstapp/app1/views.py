from django.shortcuts import render
from django.http import JsonResponse
from app1 .models import Employee

# Create your views here.
# function base view
def employeView(request):
    emp={
        'id':123,
        'name':'Ashish',
        'salary': 10000000
    }

    data=Employee.objects.all();
    response={'employes':list(data.values('name','sal'))}
    return JsonResponse(response)
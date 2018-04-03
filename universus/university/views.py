from django.shortcuts import render
from suds.client import Client

# Create your views here.

def university(request, university_id):
    client = Client('http://www.universus-webservice.ru/WebService1.asmx?WSDL')
    university = client.service.getUniversityById(int(university_id))
    departments = client.service.getAllDepartmentsByUniversityIdLite(int(university_id))
    return render(request, 'university/university.html', {
        'university': university,
        'departments': departments.Department if departments else None})

def university_list(request):
    client = Client('http://www.universus-webservice.ru/WebService1.asmx?WSDL')
    result = client.service.getAllUniversitiesLite()
    return render(request, 'university/university_list.html', { 'universities': result.University })

def university_list_delete(request):
    return render(request, 'university/university_list_delete.html', locals())

def university_add(request):
    return render(request, 'university/university_add.html', locals())

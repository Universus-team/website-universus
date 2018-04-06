from django.shortcuts import render
from suds.client import Client
# Create your views here.

def teachers(request):
    client = Client('http://www.universus-webservice.ru/WebService1.asmx?WSDL')
    te = client.service.getAllTeachers()
    dp = []
    uni = []
    for s in te.Account:
        d = client.service.getDepartmentByIdLite(s.DepartmentId)
        dp.append(d)
        uni.append(client.service.getUniversityByIdLite(d.UniversityId))
    data = zip(te.Account, uni, dp)
    return render(request, 'teachers/teachers.html', {'data': data})
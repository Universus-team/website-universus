from django.shortcuts import render
from suds.client import Client


# Create your views here.


def department_add(request):
    return render(request, 'department/department_add.html', locals())


def department_delete(request):
    return render(request, 'department/department_delete.html', locals())


def department(request, department_id):
    client = Client('http://www.universus-webservice.ru/WebService1.asmx?WSDL')
    depart = client.service.getDepartmentById(int(department_id))
    groups = client.service.getAllStudentGroupByDepartmentIdLite(int(department_id))
    return render(request, "department/department.html", {
        'department': depart ,
        'groups' : groups.StudentGroup if groups else None});

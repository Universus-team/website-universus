from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from suds.client import Client
from suds.sax.attribute import Attribute
from suds.sax.element import Element
import json


# Create your views here.


def department_add(request, university_id):
    client = Client('http://www.universus-webservice.ru/WebService1.asmx?WSDL')
    uni = client.service.getUniversityByIdLite(university_id)
    if request.method == 'POST':
        depart = client.factory.create('Department')
        auth = Element("AuthHeader").append((
            Element('Email').setText(request.session.get('email', '')),
            Element('Password').setText(request.session.get('password', '')),
            Attribute('xmlns', 'http://universus-webservice.ru/'))
        )
        client.set_options(soapheaders=auth)
        depart.Id = 0;
        depart.Name = request.POST.get('name')
        depart.Description = request.POST.get('description', '')
        depart.DeanName = request.POST.get('dean', '')
        depart.UniversityId = university_id
        result = client.service.addDepartment(depart)
        return render(request, 'department/department_add.html', {'university': uni,
                                                                  'result': result})
    return render(request, 'department/department_add.html', {'university': uni})


def department_delete(request, department_id):
    client = Client('http://www.universus-webservice.ru/WebService1.asmx?WSDL')
    auth = Element("AuthHeader").append((
        Element('Email').setText(request.session.get('email', '')),
        Element('Password').setText(request.session.get('password', '')),
        Attribute('xmlns', 'http://universus-webservice.ru/'))
    )
    client.set_options(soapheaders=auth)
    dep = client.service.getDepartmentByIdLite(department_id)
    uni = client.service.getUniversityByIdLite(dep.UniversityId)
    result = client.service.deleteDepartmentById(department_id)
    return render(request, 'department/department_delete.html', {'result': result,
                                                                 'university': uni,
                                                                 'department': dep})


@csrf_exempt
def department(request, department_id):
    client = Client('http://www.universus-webservice.ru/WebService1.asmx?WSDL')
    auth = Element("AuthHeader").append((
        Element('Email').setText(request.session.get('email', '')),
        Element('Password').setText(request.session.get('password', '')),
        Attribute('xmlns', 'http://universus-webservice.ru/'))
    )
    client.set_options(soapheaders=auth)
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        dept = json.loads(data)
        depart = client.service.getDepartmentById(department_id)
        depart.Name = dept['name']
        depart.Description = dept['description']
        depart.DeanName = dept['dean_name']
        result = client.service.updateDepartment(depart)
    depart = client.service.getDepartmentById(int(department_id))
    groups = client.service.getAllStudentGroupByDepartmentIdLite(int(department_id))
    role_id = request.session.get('role_id', 0)
    return render(request, "department/department.html", {
        'department': depart,
        'groups': groups.StudentGroup if groups else None,
        'role_id': role_id});

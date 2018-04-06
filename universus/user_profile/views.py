from django.shortcuts import render
from suds.client import Client
from suds.sax.attribute import Attribute
from suds.sax.element import Element


# Create your views here.
from user_profile.util import getRoleById


def show_profile(request):
    if request.session.get('id', False):
        client = Client('http://www.universus-webservice.ru/WebService1.asmx?WSDL')
        auth = Element("AuthHeader").append((
            Element('Email').setText(request.session.get('email', '')),
            Element('Password').setText(request.session.get('password', '')),
            Attribute('xmlns', 'http://universus-webservice.ru/'))
        )
        client.set_options(soapheaders=auth)
        account = client.service.getAccount()
        department = client.service.getDepartmentByIdLite(account.DepartmentId)
        university = client.service.getUniversityByIdLite(department.UniversityId)
        role = getRoleById(account.RoleId)
    return render(request, 'user_profile/user_profile.html', {'account' : account,
                                                              'role':role,
                                                              'university': university,
                                                              'department': department});


def show_profile_by_id(request, account_id):
    if request.session.get('id', False):
        client = Client('http://www.universus-webservice.ru/WebService1.asmx?WSDL')
        account = client.service.getAccountById(int(account_id))
        department = client.service.getDepartmentByIdLite(account.DepartmentId)
        university = client.service.getUniversityByIdLite(department.UniversityId)
        role = getRoleById(account.RoleId)
    return render(request, 'user_profile/user_profile_id.html', {'account' : account,
                                                              'role':role,
                                                              'university': university,
                                                              'department': department,
                                                              'role_id' : request.session.get('role_id', 0)});

def delete_user_profile(request, account_id):
    client = Client('http://www.universus-webservice.ru/WebService1.asmx?WSDL')
    auth = Element("AuthHeader").append((
        Element('Email').setText(request.session.get('email', '')),
        Element('Password').setText(request.session.get('password', '')),
        Attribute('xmlns', 'http://universus-webservice.ru/'))
    )
    client.set_options(soapheaders=auth)
    acc = client.service.getAccountById(int(account_id))
    result = client.service.deleteAccountById(int(account_id))
    return render(request, 'user_profile/user_profile_delete.html',
                  {'result': result,
                   'profile': acc})
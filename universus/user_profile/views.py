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
from cloudinary.templatetags import cloudinary
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from suds.client import Client
from suds.sax.attribute import Attribute
from suds.sax.element import Element


# Create your views here.
from user_profile.util import getRoleById
import json

@csrf_exempt
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

        if request.method == 'POST':
            data = request.body.decode('utf-8')
            acc = json.loads(data)
            account.Name = acc['name']
            account.Surname = acc['surname']
            account.Patronymic = acc['patronymic']
            account.Address = acc['address']
            account.Phone = acc['phone']
            account.BirthDay = acc['birth_day']
            res = client.service.updateAccount(account)
            print(res)
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

def add_user_profile(request):
    client = Client('http://www.universus-webservice.ru/WebService1.asmx?WSDL')
    auth = Element("AuthHeader").append((
        Element('Email').setText(request.session.get('email', '')),
        Element('Password').setText(request.session.get('password', '')),
        Attribute('xmlns', 'http://universus-webservice.ru/'))
    )
    client.set_options(soapheaders=auth)

    if request.method == 'POST':
        account = client.factory.create('Account')
        account.Id = 0
        account.Name = request.POST['name']
        account.Surname = request.POST['surname']
        account.Patronymic = request.POST['patronymic'] if request.POST['patronymic'] else ' '
        account.Address = request.POST['address'] if request.POST['address'] else 'не задан'
        account.Email = request.POST['email']
        account.Phone = request.POST['phone'] if request.POST['phone'] else 'не задан'
        account.PasswordMD5 = request.POST['password']
        account.DepartmentId = request.POST['department']
        account.BirthDay = request.POST['birth_day']
        account.RoleId = request.POST['role'];

        if request.FILES and request.FILES['photo']:
            cloudinary.config(
                cloud_name="universusimages",
                api_key="421689719673152",
                api_secret="E3pIIQne8HbWnxnJiyNm9NFGCxY"
            )
            account.PhotoURL = cloudinary.uploader.upload(
                request.FILES['photo'].read(),
                crop='fit',
                width=700,
                height=700
            )['url']
        else:
            account.PhotoURL = 'http://res.cloudinary.com/universusimages/image/upload/v1523119802/default.png'
        id = client.service.addStudent(account)
        if id > 0:
            request.session['id'] = id
            request.session['email'] = account.Email
            request.session['password'] = account.PasswordMD5
            request.session['role_id'] = account.RoleId
            return HttpResponseRedirect('/profile_/show/'+str(id))

    uni = client.service.getAllUniversitiesLite()
    role_id = request.session.get('role_id', 0)
    return render(request, 'user_profile/add_profile.html', {
        'universities': uni.University if uni else [],
        'role_id': role_id})
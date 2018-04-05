from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import json

from django.views.decorators.csrf import csrf_exempt
from suds.client import Client
from suds.sax.attribute import Attribute
from suds.sax.element import Element
import cloudinary
import cloudinary.uploader
import cloudinary.api

@csrf_exempt
def singup(request):
   client = Client('http://www.universus-webservice.ru/WebService1.asmx?WSDL')
   if request.method == 'POST':
       account = client.factory.create('Account')
       account.Id = 0
       account.Name = request.POST.get('name', '')
       account.Surname = request.POST.get('surname', '')
       account.Patronymic = request.POST.get('patronymic', '')
       account.Address = request.POST.get('address', '')
       account.Email = request.POST.get('email', '')
       account.Phone = request.POST.get('phone', '')
       account.PasswordMD5 = request.POST.get('password', '')
       account.DepartmentId = request.POST.get('department', 1)
       account.BirthDay = request.POST.get('birth_day', '')
       account.RoleId = 1;

       if request.FILES['photo']:
            cloudinary.config(
                 cloud_name="universusimages",
                 api_key="421689719673152",
                 api_secret="E3pIIQne8HbWnxnJiyNm9NFGCxY"
            )
            account.PhotoURL = cloudinary.uploader.upload(
                 request.FILES['photo'].read(),
                 crop = 'fit',
                 width = 700,
                 height = 700
            )['url']
       id = client.service.addStudent(account)
       if id > 0:
             request.session['id'] = id
             request.session['email'] = account.Email
             request.session['password'] = account.PasswordMD5
             request.session['role_id'] = account.RoleId
             return HttpResponseRedirect('/profile_')


   uni = client.service.getAllUniversitiesLite()
   return render(request, 'singup/singup.html', {'universities' : uni.University})

@csrf_exempt
def departments(request):
   client = Client('http://www.universus-webservice.ru/WebService1.asmx?WSDL')
   if request.method == 'POST':
      ajax_data = json.loads(request.body.decode('utf-8'))
      dps = client.service.getAllDepartmentsByUniversityIdLite(ajax_data['university_id'])
      depart = [{'Name': d.Name, 'Id': d.Id} for d in dps.Department]
      return HttpResponse(json.dumps(depart), content_type='application/json')

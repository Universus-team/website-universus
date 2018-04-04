from django.http import HttpResponse
from django.shortcuts import render
import json

from django.views.decorators.csrf import csrf_exempt
from suds.client import Client
from suds.sax.attribute import Attribute
from suds.sax.element import Element

@csrf_exempt
def singup(request):
   client = Client('http://www.universus-webservice.ru/WebService1.asmx?WSDL')
   if request.method == 'POST':
      ajax_data = json.loads(request.body.decode('utf-8'))
      dps = client.service.getAllDepartmentsByUniversityIdLite(ajax_data['university_id'])
      depart = [{'Name' :d.Name, 'Id': d.Id} for d in dps.Department]
      return HttpResponse(json.dumps(depart), content_type='application/json')
   uni = client.service.getAllUniversitiesLite()
   return render(request, 'singup/singup.html', {'universities' : uni.University})

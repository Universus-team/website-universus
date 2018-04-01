from django.shortcuts import render
from suds.client import Client

# Create your views here.


def test_webservice(request):
    client = Client('http://www.universus-webservice.ru/WebService1.asmx?WSDL')
    result = client.service.test('universus')
    username = client.service.getUsernameById(1)
    return render(request, 'test_webservice/test_webservice.html', locals())
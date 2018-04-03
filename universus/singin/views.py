from django.http import HttpResponseRedirect
from django.shortcuts import render
from suds.client import Client
from suds.sax.attribute import Attribute
from suds.sax.element import Element

# Create your views here.
def singin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        client = Client('http://www.universus-webservice.ru/WebService1.asmx?WSDL')
        auth = Element("AuthHeader").append((
            Element('Email').setText(email),
            Element('Password').setText(password),
            Attribute('xmlns', 'http://universus-webservice.ru/'))
        )
        client.set_options(soapheaders=auth)
        id = client.service.getId()
        if (id > 0):
            request.session['id'] = id
            request.session['email'] = email
            request.session['password'] = password
            return HttpResponseRedirect('/profile_')
        else:
            return render(request, 'singin/singin.html', {'result': False})
    return render(request, 'singin/singin.html', {'result': True})
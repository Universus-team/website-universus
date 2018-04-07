from django.http import HttpResponseRedirect
from django.shortcuts import render
from suds.client import Client
from suds.sax.attribute import Attribute
from suds.sax.element import Element

# Create your views here.
def singin(request):
    if request.session.get('email', False):
        return HttpResponseRedirect('/profile_')

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
            account = client.service.getAccount()
            request.session['id'] = id
            request.session['email'] = email
            request.session['password'] = password
            request.session['role_id'] = account.RoleId
            return HttpResponseRedirect('/profile_')
        else:
            return render(request, 'singin/singin.html', {'result': False})
    return render(request, 'singin/singin.html', {'result': True})

def logout(request):
    del request.session['id']
    del request.session['email']
    del request.session['password']
    del request.session['role_id']
    return HttpResponseRedirect('/')
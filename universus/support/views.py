from django.shortcuts import render
from suds.client import Client
# Create your views here.

def support(request):
    client = Client('http://www.universus-webservice.ru/WebService1.asmx?WSDL')
    mods = client.service.getAllModerators()
    return render(request, "support/support.html", {'moderators': mods.Account if mods else []})
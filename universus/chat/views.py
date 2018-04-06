from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from suds.client import Client
from suds.sax.attribute import Attribute
from suds.sax.element import Element
import json
# Create your views here.


def my_dialogs(request):
    return render(request, 'chat/my_dialogs.html', locals())

@csrf_exempt
def dialog(request, to_user_id):
    client = Client('http://www.universus-webservice.ru/WebService1.asmx?WSDL')
    auth = Element("AuthHeader").append((
        Element('Email').setText(request.session.get('email', '')),
        Element('Password').setText(request.session.get('password', '')),
        Attribute('xmlns', 'http://universus-webservice.ru/'))
    )
    client.set_options(soapheaders=auth)
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        query = json.loads(data)
        response = {}
        if query['sendMessage']:
            response['result_send'] = client.service.sendMessage(int(to_user_id), query['message'])
        if query['getDialog']:
            msgs = client.service.getDialog(request.session.get('id', 0))
            response['dialog'] = msgs.Message
        return HttpResponse(json.dumps(response), content_type='application/json')
    return render(request, 'chat/dialog.html', {})





from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from flask import json
from suds.client import Client
from suds.sax.attribute import Attribute
from suds.sax.element import Element
# Create your views here.


def my_dialogs(request):
    client = Client('http://www.universus-webservice.ru/WebService1.asmx?WSDL')
    auth = Element("AuthHeader").append((
        Element('Email').setText(request.session.get('email', '')),
        Element('Password').setText(request.session.get('password', '')),
        Attribute('xmlns', 'http://universus-webservice.ru/'))
    )
    client.set_options(soapheaders=auth)
    dialogs = client.service.getDialogs()
    countMsgs = []
    lastMsgs = []
    for account in dialogs.Account:
        countMsgs.append(client.service.getCountNewMessages(account.Id))
        lastMsgs.append(client.service.getLastMessage(account.Id))
    data = zip(dialogs.Account, countMsgs, lastMsgs)
    return render(request, 'chat/my_dialogs.html', {'dialogs': data})

@csrf_exempt
def dialog(request, to_user_id):
    client = Client('http://www.universus-webservice.ru/WebService1.asmx?WSDL')
    auth = Element("AuthHeader").append((
        Element('Email').setText(request.session.get('email', '')),
        Element('Password').setText(request.session.get('password', '')),
        Attribute('xmlns', 'http://universus-webservice.ru/'))
    )
    client.set_options(soapheaders=auth)
    account = client.service.getAccount()
    interlocutor = client.service.getAccountById(int(to_user_id))
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        query = json.loads(data)
        response = {}
        if query['sendMessage']:
            response['result_send'] = client.service.sendMessage(int(to_user_id), query['message'])
        if query['getDialog']:
            msgs = client.service.getDialog(int(to_user_id))
            list_msgs = [{'From': x.FromUserId, 'Message': x.MessageContent, 'Date': x.DateOfMessage}
                         for x in msgs.Message]
            response['dialog'] = list_msgs
        if query['getNewMessages']:
            count = client.service.getCountNewMessages(int(to_user_id))
            if count:
                response['newMessage'] = True
                msgs = client.service.getNewMessages(int(to_user_id))
                list_msgs = [{'From': x.FromUserId, 'Message': x.MessageContent, 'Date': x.DateOfMessage}
                             for x in msgs.Message]
                response['messages'] = list_msgs
        return HttpResponse(json.dumps(response), content_type='application/json')
    return render(request, 'chat/dialog.html', {'account': account,
                                                'interlocutor': interlocutor})




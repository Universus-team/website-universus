import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime

from suds.client import Client
from suds.sax.attribute import Attribute
from suds.sax.element import Element

@csrf_exempt
def exam_buider(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        exam = json.loads(data)
        client = Client('http://www.universus-webservice.ru/WebService1.asmx?WSDL')
        auth = Element("AuthHeader").append((
            Element('Email').setText(request.session.get('email', '')),
            Element('Password').setText(request.session.get('password', '')),
            Attribute('xmlns', 'http://universus-webservice.ru/'))
        )
        client.set_options(soapheaders=auth)

        exm = client.factory.create('Exam')
        exm.Id = 0
        exm.Title = exam['title']
        exm.Description = exam['description']
        exm.AuthorId = client.service.getId()
        exm.CountOfQuestion = len(exam['tests'])
        exm.Content = json.dumps(exam['tests'])
        res = client.service.addExam(exm)
        response = {
            'status': res,
            'message': 'Сохранено '+datetime.strftime(datetime.now(), '%H:%M:%S')
        }
        return HttpResponse(json.dumps(response), content_type='application/json')
    return render(request, 'exam_builder/exam_builder.html', locals())

def exam_list(request):
    client = Client('http://www.universus-webservice.ru/WebService1.asmx?WSDL')
    auth = Element("AuthHeader").append((
        Element('Email').setText(request.session.get('email', '')),
        Element('Password').setText(request.session.get('password', '')),
        Attribute('xmlns', 'http://universus-webservice.ru/'))
    )
    client.set_options(soapheaders=auth)
    account = client.service.getAccount()
    exams = client.service.getAllExamsByDepartmentId(account.DepartmentId)

    return render(request, 'exam_builder/exam_list.html', {
        'exams': exams.Exam if exams else []
    })


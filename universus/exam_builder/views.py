import json

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime

from suds.client import Client
from suds.sax.attribute import Attribute
from suds.sax.element import Element
import json


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
    role_id = request.session.get('role_id', 0)
    id = request.session.get('id', 0)
    if role_id == 2:
        account = client.service.getAccount()
        exams = client.service.getAllExamsByDepartmentId(account.DepartmentId)
        return render(request, 'exam_builder/exam_list.html', {
            'exams': exams.Exam if exams else [],
            'role_id': role_id
        })
    else:
        tests = client.service.getAllExamHistoryByStudentId(id)
        return render(request, 'exam_builder/exam_history_list_student.html',
                      {'tests': tests.ExamHistory if tests else []})

def exam_show(request, exam_id):
    client = Client('http://www.universus-webservice.ru/WebService1.asmx?WSDL')
    auth = Element("AuthHeader").append((
        Element('Email').setText(request.session.get('email', '')),
        Element('Password').setText(request.session.get('password', '')),
        Attribute('xmlns', 'http://universus-webservice.ru/'))
    )
    client.set_options(soapheaders=auth)
    exam = client.service.getExamById(int(exam_id))
    tests = json.loads(exam.Content)
    return render(request, 'exam_builder/exam_show.html', {'exam': exam,
                                                           'tests': tests})

def choose_group(request, exam_id):
    client = Client('http://www.universus-webservice.ru/WebService1.asmx?WSDL')
    auth = Element("AuthHeader").append((
        Element('Email').setText(request.session.get('email', '')),
        Element('Password').setText(request.session.get('password', '')),
        Attribute('xmlns', 'http://universus-webservice.ru/'))
    )
    client.set_options(soapheaders=auth)
    account = client.service.getAccount()
    groups = client.service.getAllGroupsByTeacherId(account.Id)
    data = []
    dept = []
    uni = []
    if groups:
        for group in groups.StudentGroup:
            d = client.service.getDepartmentByIdLite(group.DepartmentID)
            dept.append(d)
            uni.append(client.service.getUniversityByIdLite(d.UniversityId))
        data = zip(groups.StudentGroup, dept, uni)
    return render(request, 'exam_builder/group_list_chooser.html', {'data': data,
                                                                    'exam_id': exam_id})

def set_test(request, group_id, exam_id):
    client = Client('http://www.universus-webservice.ru/WebService1.asmx?WSDL')
    auth = Element("AuthHeader").append((
        Element('Email').setText(request.session.get('email', '')),
        Element('Password').setText(request.session.get('password', '')),
        Attribute('xmlns', 'http://universus-webservice.ru/'))
    )
    client.set_options(soapheaders=auth)
    group = client.service.getStudentGroupByIdLite(int(group_id))
    exam = client.service.getExamById(int(exam_id))
    if request.method == 'POST':
        exam_history = client.factory.create('ExamHistory')
        exam_history.Id = 0
        exam_history.ExamId = int(exam_id)
        exam_history.Exam = None
        exam_history.TeacherId = request.session.get('id', 0)
        exam_history.StatusId = 1
        exam_history.Result = 0
        exam_history.DateOfTest = '1970-01-01'
        exam_history.PassingScore = int(request.POST['passing_score']) / 100
        deadline = datetime.strptime(request.POST['deadline_date'], "%Y-%m-%d")
        time = datetime.strptime(request.POST['deadline_time'], "%H:%M")
        # deadline.replace(hour=time.hour, minute=time.minute)
        exam_history.Deadline = deadline.strftime("%Y-%m-%d")
        students = client.service.getAllStudentsByGroupId(int(group_id))
        res = 0
        if students:
            for student in students.Account:
                exam_history.StudentId = student.Id
                res += client.service.addExamHistory(exam_history)
    return render(request, 'exam_builder/set_test.html', {
        'exam': exam,
        'group': group
    })

@csrf_exempt
def solve_test(request, exam_history_id):
    client = Client('http://www.universus-webservice.ru/WebService1.asmx?WSDL')
    auth = Element("AuthHeader").append((
        Element('Email').setText(request.session.get('email', '')),
        Element('Password').setText(request.session.get('password', '')),
        Attribute('xmlns', 'http://universus-webservice.ru/'))
    )
    client.set_options(soapheaders=auth)

    exam_history = client.service.getExamHistoryById(int(exam_history_id))
    exam = exam_history.Exam
    id = request.session.get('id', 0)
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        exam_history.Exam.Content = data
        res = client.service.takeExam(exam_history)
        return HttpResponseRedirect('/exambuilder_/list')
    tests = json.loads(exam.Content)
    return render(request, 'exam_builder/solve_exam.html', {'exam': exam,
                                                            'tests': tests})



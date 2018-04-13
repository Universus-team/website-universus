from django.http import HttpResponseRedirect
from django.shortcuts import render
from suds.client import Client
from suds.sax.attribute import Attribute
from suds.sax.element import Element

def main(request):
    if not request.session.get('email', False):
        return HttpResponseRedirect('/')
    # формируем ссылку для фрейма
    content_src = request.path[:request.path.index('_')+1] + 'body' + request.path[request.path.index('_')+1:]

    client = Client('http://www.universus-webservice.ru/WebService1.asmx?WSDL')
    auth = Element("AuthHeader").append((
        Element('Email').setText(request.session.get('email', '')),
        Element('Password').setText(request.session.get('password', '')),
        Attribute('xmlns', 'http://universus-webservice.ru/'))
    )
    client.set_options(soapheaders=auth)
    dep_id = request.session.get('department_id', False)
    if not dep_id:
        account = client.service.getAccount()
        dep_id = account.DepartmentId
    dep = client.service.getDepartmentByIdLite(dep_id)
    uni = client.service.getUniversityByIdLite(dep.UniversityId)
    count_msg = 0;
    dialogs = client.service.getDialogs()
    if (dialogs):
        for account in dialogs.Account:
            count_msg += client.service.getCountNewMessages(account.Id)

    role_id = request.session.get('role_id', 0)
    id = request.session.get('id', 0)
    tests = []
    if role_id == 1:
        tests = client.service.getAllExamHistoryByStudentId(id)
    return render(request, 'main/main.html', {'university': uni,
                                              'content_src': content_src,
                                              'count_msg': count_msg,
                                              'role_id': role_id,
                                              'tests': tests.ExamHistory if tests else []})
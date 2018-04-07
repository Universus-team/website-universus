from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from suds.client import Client
from suds.sax.attribute import Attribute
from suds.sax.element import Element
import json

# Create your views here.

def my_groups(request):
    client = Client('http://www.universus-webservice.ru/WebService1.asmx?WSDL')
    auth = Element("AuthHeader").append((
        Element('Email').setText(request.session.get('email', '')),
        Element('Password').setText(request.session.get('password', '')),
        Attribute('xmlns', 'http://universus-webservice.ru/'))
    )
    client.set_options(soapheaders=auth)
    account = client.service.getAccount()
    groups = []
    if account.RoleId == 1: #if student
        groups = client.service.getAllGroupsByStudentId(account.Id)
    if account.RoleId == 2: #if teacher
        groups = client.service.getAllGroupsByTeacherId(account.Id)
    data = []
    dept = []
    uni = []
    if groups:
        if len(groups.StudentGroup) == 1:
            return HttpResponseRedirect('/studentgroup_body/show/' + str(groups.StudentGroup[0].Id) + '/')
        for group in groups.StudentGroup:
            d = client.service.getDepartmentByIdLite(group.DepartmentID)
            dept.append(d)
            uni.append(client.service.getUniversityByIdLite(d.UniversityId))
        data = zip(groups.StudentGroup, dept, uni)
    return render(request, 'student_group/group_list.html', {'data' : data})

def student_group(request, group_id):
    client = Client('http://www.universus-webservice.ru/WebService1.asmx?WSDL')
    group = client.service.getStudentGroupById(int(group_id))
    students = client.service.getAllStudentsByGroupId(int(group_id))
    teachers = client.service.getAllTeachersByGroupId(int(group_id))
    role_id = request.session.get('role_id', 0)
    return render(request, 'student_group/student_group.html',
                  {'group': group,
                   'role_id': role_id,
                   'students': students.Account if students else [],
                   'teachers': teachers.Account if teachers else []})

def add_student_to_group(request, group_id):
    client = Client('http://www.universus-webservice.ru/WebService1.asmx?WSDL')
    st = client.service.getAllStudents()
    students = [x for x in st.Account if not client.service.isStudentMemberOfGroup(x.Id, int(group_id))]
    group = client.service.getStudentGroupById(int(group_id))
    dp = []
    uni = []
    for s in students:
        d = client.service.getDepartmentByIdLite(s.DepartmentId)
        dp.append(d)
        uni.append(client.service.getUniversityByIdLite(d.UniversityId))
    data = zip(students, uni, dp)
    return render(request, 'student_group/add_student.html', {'data': data, 'group': group})

def delete_student(request, group_id, student_id):
    client = Client('http://www.universus-webservice.ru/WebService1.asmx?WSDL')
    auth = Element("AuthHeader").append((
        Element('Email').setText(request.session.get('email', '')),
        Element('Password').setText(request.session.get('password', '')),
        Attribute('xmlns', 'http://universus-webservice.ru/'))
    )
    client.set_options(soapheaders=auth)
    group = client.service.getStudentGroupById(int(group_id))
    account = client.service.getAccountById(int(student_id))
    result = client.service.deleteStudentFromGroup(int(student_id), int(group_id))
    return render(request, 'student_group/delete_student.html', {'group': group, 'account': account, 'result': result})


def added_student_to_group(request, group_id, student_id):
    client = Client('http://www.universus-webservice.ru/WebService1.asmx?WSDL')
    auth = Element("AuthHeader").append((
        Element('Email').setText(request.session.get('email', '')),
        Element('Password').setText(request.session.get('password', '')),
        Attribute('xmlns', 'http://universus-webservice.ru/'))
    )
    client.set_options(soapheaders=auth)
    group = client.service.getStudentGroupById(int(group_id))
    account = client.service.getAccountById(int(student_id))
    result = client.service.addStudentToGroup(int(student_id), int(group_id))
    return render(request, 'student_group/added_student.html', {'group': group, 'account': account, 'result': result})
from django.shortcuts import render
from suds.client import Client


# Create your views here.
def student_group(request, group_id):
    client = Client('http://www.universus-webservice.ru/WebService1.asmx?WSDL')
    group = client.service.getStudentGroupById(int(group_id))
    return render(request, 'student_group/student_group.html', {'group': group})
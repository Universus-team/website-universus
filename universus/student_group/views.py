from django.shortcuts import render
from suds.client import Client
from suds.sax.attribute import Attribute
from suds.sax.element import Element

# Create your views here.
def student_group(request, group_id):
    client = Client('http://www.universus-webservice.ru/WebService1.asmx?WSDL')
    group = client.service.getStudentGroupById(int(group_id))
    role_id = request.session.get('role_id', 0)
    return render(request, 'student_group/student_group.html', {'group': group, 'role_id': role_id})


def add_student_to_group(request, group_id):
    client = Client('http://www.universus-webservice.ru/WebService1.asmx?WSDL')
    st = client.service.getAllStudents()
    group = client.service.getStudentGroupById(int(group_id))
    dp = []
    uni = []
    for s in st.Account:
        d = client.service.getDepartmentByIdLite(s.DepartmentId)
        dp.append(d)
        uni.append(client.service.getUniversityByIdLite(d.UniversityId))
    data = zip(st.Account, uni, dp)
    return render(request, 'students/students.html', {'data': data, 'group': group})
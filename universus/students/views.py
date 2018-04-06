from django.shortcuts import render
from suds.client import Client
# Create your views here.


def students(request):
    client = Client('http://www.universus-webservice.ru/WebService1.asmx?WSDL')
    st = client.service.getAllStudents()
    dp = []
    uni = []
    for s in st.Account:
        d = client.service.getDepartmentByIdLite(s.DepartmentId)
        dp.append(d)
        uni.append(client.service.getUniversityByIdLite(d.UniversityId))
    data = zip(st.Account, uni, dp)
    return render(request, 'students/students.html', {'data': data})
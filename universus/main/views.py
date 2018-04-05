from django.shortcuts import render
from suds.client import Client

# Create your views here.
def main(request):
    # формируем ссылку для фрейма
    content_src = request.path[:request.path.index('_')+1] + 'body' + request.path[request.path.index('_')+1:]
    client = Client('http://www.universus-webservice.ru/WebService1.asmx?WSDL')
    dep_id = request.session.get('department_id', False)
    if (dep_id):
        dep = client.service.getDepartmentByIdLite(dep_id)
        uni = client.service.getUniversityByIdLite(dep.UniversityId)
        return render(request, 'main/main.html', {'university' : uni, 'content_src' : content_src})
    return render(request, 'main/main.html', {'content_src' : content_src})
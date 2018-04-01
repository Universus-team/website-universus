from django.shortcuts import render

# Create your views here.

def university(request):
    return render(request, 'university/university.html', locals())

def university_list(request):
    client = Client('http://www.universus-webservice.ru/WebService1.asmx?WSDL')
    result = client.service.test('universus')
    username = client.service.getUsernameById(1)
    return render(request, 'university/university_list.html', locals())

def university_list_delete(request):
    return render(request, 'university/university_list_delete.html', locals())

def university_add(request):
    return render(request, 'university/university_add.html', locals())

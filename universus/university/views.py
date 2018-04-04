from django.shortcuts import render
from suds.client import Client
import cloudinary
import cloudinary.uploader
import cloudinary.api
from suds.sax.attribute import Attribute
from suds.sax.element import Element

# Create your views here.

def university(request, university_id):
    client = Client('http://www.universus-webservice.ru/WebService1.asmx?WSDL')
    university = client.service.getUniversityById(int(university_id))
    departments = client.service.getAllDepartmentsByUniversityIdLite(int(university_id))
    role_id = request.session.get('role_id', 0)
    return render(request, 'university/university.html', {
        'university': university,
        'departments': departments.Department if departments else None,
        'role_id': role_id})

def university_list(request):
    client = Client('http://www.universus-webservice.ru/WebService1.asmx?WSDL')
    result = client.service.getAllUniversitiesLite()
    role_id = request.session.get('role_id', 0)
    return render(request, 'university/university_list.html', {
        'universities': result.University,
        'role_id': role_id})

def university_delete(request, university_id):
    client = Client('http://www.universus-webservice.ru/WebService1.asmx?WSDL')
    auth = Element("AuthHeader").append((
        Element('Email').setText(request.session.get('email', '')),
        Element('Password').setText(request.session.get('password', '')),
        Attribute('xmlns', 'http://universus-webservice.ru/'))
    )
    client.set_options(soapheaders=auth)
    uni = client.service.getUniversityById(university_id)
    result = client.service.deleteUniversityById(university_id)
    return render(request, 'university/university_delete.html',
                  {'result': result,
                   'university': uni})

def university_add(request):
    if request.method == 'POST':
        cloudinary.config(
            cloud_name="universusimages",
            api_key="421689719673152",
            api_secret="E3pIIQne8HbWnxnJiyNm9NFGCxY"
        )
        client = Client('http://www.universus-webservice.ru/WebService1.asmx?WSDL')
        University = client.factory.create('University')
        auth = Element("AuthHeader").append((
            Element('Email').setText(request.session.get('email', '')),
        Element('Password').setText(request.session.get('password', '')),
        Attribute('xmlns', 'http://universus-webservice.ru/'))
        )
        client.set_options(soapheaders=auth)
        University['Id'] = 0;
        University['FullName'] = request.POST.get('full_name')
        University['ShortName'] = request.POST.get('short_name')
        University['Address'] = request.POST.get('address')
        University['WebSite'] = request.POST.get('web_site')
        University['Description'] = request.POST.get('description', '')
        logo_url = cloudinary.uploader.upload(
              request.FILES['logo'].read(),
              crop = 'fit',
              width = 500,
              height = 500
        )['url']
        University['LogoURL'] = logo_url
        client.service.addUniversity(University)
        return render(request, 'university/university_add.html', {'added' : True})
    return render(request, 'university/university_add.html', locals())


# ,eager=[{"width": 400, "height": 300, "crop": "fit"}]
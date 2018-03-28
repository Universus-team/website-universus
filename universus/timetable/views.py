from django.http import HttpResponse
from django.shortcuts import render
# from flask import json



# Create your views here.
from webservice import webservice


def get_timetable(request):
    list(filter(
        lambda x: True,
        webservice.getTimetable()
    ))
    return HttpResponse(json.dump([]), content_type='application/json', status=200)

def timetable(request):
    return render(request, 'timetable/timetable.html', locals());
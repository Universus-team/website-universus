from django.http import HttpResponse
from django.shortcuts import render
# from flask import json



# Create your views here.



def timetable(request):
    return render(request, 'timetable/timetable.html', locals());
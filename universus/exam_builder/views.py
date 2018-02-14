import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime

@csrf_exempt
def exam_buider(request):
    if request.method == 'POST':
        data = request.body
        print(data)
        response = {
            'status': 1,
            'message': 'Сохранено '+datetime.strftime(datetime.now(), '%H:%M:%S')
        }
        return HttpResponse(json.dumps(response), content_type='application/json')
    return render(request, 'exam_builder/exam_builder.html', locals())



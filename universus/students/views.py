from django.shortcuts import render

# Create your views here.


def students(request):
    return render(request, 'students/students.html', locals())
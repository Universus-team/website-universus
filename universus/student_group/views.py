from django.shortcuts import render

# Create your views here.
def student_group(request):
    return render(request, 'student_group/student_group.html', locals())
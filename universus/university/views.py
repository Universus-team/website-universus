from django.shortcuts import render

# Create your views here.

def university(request):
    return render(request, 'university/university.html', locals())

def university_list(request):
    return render(request, 'university/university_list.html', locals())

def university_list_delete(request):
    return render(request, 'university/university_list_delete.html', locals())

def university_add(request):
    return render(request, 'university/university_add.html', locals())

def department_add(request):
    return render(request, 'university/department_add.html', locals())

def department_delete(request):
    return render(request, 'university/department_delete.html', locals())
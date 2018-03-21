from django.shortcuts import render

# Create your views here.



def department_add(request):
    return render(request, 'department/department_add.html', locals())

def department_delete(request):
    return render(request, 'department/department_delete.html', locals())

def department(request):
    return render(request, 'department/department.html', locals());
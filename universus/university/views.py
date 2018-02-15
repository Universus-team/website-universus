from django.shortcuts import render

# Create your views here.

def university(request):
    return render(request, 'university/university.html', locals())

def university_list(request):
    return render(request, 'university/university_list.html', locals())
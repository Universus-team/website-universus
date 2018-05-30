from django.shortcuts import render

# Create your views here.


def add(request):
    return render(request, 'tutorial/add.html', {})

def show(request, tutorial_id):
    return None;
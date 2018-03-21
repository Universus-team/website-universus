from django.shortcuts import render

# Create your views here.
def singin(request):
    return render(request, 'singin/singin.html', locals())
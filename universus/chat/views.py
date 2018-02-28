from django.shortcuts import render


# Create your views here.


def my_dialogs(request):
    return render(request, 'chat/my_dialogs.html', locals())


def dialog(request):
    return render(request, 'chat/dialog.html', locals())




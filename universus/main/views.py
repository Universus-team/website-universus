from django.shortcuts import render

# Create your views here.
def main(request):
    content_src = request.path + 'body'
    return render(request, 'main/main.html', locals())
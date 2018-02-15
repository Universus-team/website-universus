from django.shortcuts import render

# Create your views here.
def main(request, regex_group):
    # формируем ссылку для фрейма
    content_src = request.path[:request.path.index('_')+1] + 'body' + request.path[request.path.index('_')+1:]

    return render(request, 'main/main.html', locals())
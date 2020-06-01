from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Hello, world! </h1> <h2> This is project Dewdrop and you're at the recruitment app index. </h2>")
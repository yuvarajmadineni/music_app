from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>List of albums</h1>")

def detail(request, album_id):
    return HttpResponse("<h2>Details of the Ablum id: " + str(album_id) + "</h2>")
    

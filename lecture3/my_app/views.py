from django.shortcuts import render


# Create your views here.
def greet(request, name):
    return render(request, "my_app/index.html", {
        "name": name.capitalize()
    })


def index(request):
    return render(request, "my_app/index.html")

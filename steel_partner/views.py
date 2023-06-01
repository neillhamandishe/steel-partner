from django.shortcuts import render

def home_view(request, *args, **kwargs):
    if request.method == "GET":
        return render(request, "home.html", context={})
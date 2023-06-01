from django.shortcuts import render, redirect, resolve_url
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login

User = get_user_model()

def login(request, *args, **kwargs):
    if request.method == "GET":
        return render(request, "accounts/login.html")
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username,password=password)

        if user is None:
            return redirect(resolve_url("accounts:login"), {"errors": ["Access denied, check credentials and try again"]})
        
        login(request, user)
            
        # redirect to relevant dash
        # if user.is_superuser:
        #     return redirect("/admin")
        
        return render(request, "accounts/customer_dash.html")
   
    
def customer_dash(request, *args, **kwargs):
    if request.method == "GET":
        return render(request, "accounts/customer_dash.html", context={})

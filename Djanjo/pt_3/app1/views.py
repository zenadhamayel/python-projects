from django.shortcuts import render, HttpResponse, redirect
def index(request):
    return render(request,"index.html")
def login(request):
    return render(request,"login.html")
def check_credentials(request):
    username=request.POST["username"]
    password=request.POST["password"]
    if username=="zenad"and password=="12345":
        request.session["my_username"]=username
        return redirect("/homepage")
    else:
        return render(request,"login.html")

        
    
    
           
def go_to_homepage(request):
    return render(request,"home.html") 


from django.shortcuts import render,redirect

def index(request):
    if "count" not in request.session:
        request.session["count"] = 0
    else:
        request.session["count"] += 1
    return render(request,"index.html") 



def count(request):
    request.session["count"] += 2
    return redirect("/")


def rest(request):
    request.session.clear()
    return redirect("/")

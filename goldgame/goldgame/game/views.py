import random
from django.shortcuts import render, redirect

def index(request):
    if 'random' not in request.session:
        request.session['random']= random.randint(1,100)
    if 'result' not in request.session:
        request.session['result']=''
    context={
        'result': request.session['result'],
        'color': request.session.get('color', '')
    }
    return render(request, 'game.html', context)

def randNum(request):
    rand_num=int(request.POST['number'])
    if rand_num > request.session['random']:
        request.session['result']='too high'
        request.session['color']='blue'
    elif rand_num < request.session['random']:
        request.session['result']='too low'
        request.session['color']='red'
    else :
        request.session['result']= 'correct'
        request.session['color']='green'
    print(request.session['result'])
    print(request.session['random'])

    return redirect('/')

def clearsessions(request):
    request.session.clear()
    return redirect('/')


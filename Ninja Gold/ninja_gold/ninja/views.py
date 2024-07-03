import random
from django.shortcuts import render,redirect
from datetime import datetime

# Create your views here.
import random
from django.shortcuts import render,redirect
from datetime import datetime

# Create your views here.
def index(request):  
    if 'gold' not in request.session:
        request.session['gold']=0 
        request.session['activities']=[]
    ninja_dic={
        'gold':request.session['gold'],
        'activities':request.session['activities']
    }
    return render(request,'index.html', ninja_dic)

def process_money(request):
    building =request.POST['building']
    if building =='farm':
        earn_gold=random.randint(10,20)
    elif building =='casino':
        earn_gold=random.randint(-50,50)
    request.session['gold']+=earn_gold
    time= datetime.now().strftime('%d%Y-%H%M')
    if earn_gold >=0:
        activity=f'Earned {earn_gold} form{building} on {time}'
    else:
        activity=f'Lost {earn_gold} form{building} on {time}'
    request.session['activities'].append(activity)
    print(activity)
    return redirect('/')  

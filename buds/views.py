from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import json
from django.core import serializers


# Create your views here.
def home(request):
    return render(request, 'home.html')

def register(request):
    # success_url = reverse_lazy('home.html')
    return render(request, 'signup.html')

def login(request):
    # success_url = reverse_lazy('index.html')
    return render(request, 'signin.html')

def dashboard(request):
    return render(request, 'index.html')

def expenses(request):
    return render(request, 'budget.html')

# def user_form(request):
#     if request.method == 'POST':
#         username = request.POST.get('u_name')
#         user = User(username=username)
#         user.save()
#         return redirect('dashboard')
#     return render(request, 'login.html')

def register_det(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.create_user(username, email, password)
        user.save()
        return render(request,'signin.html')
    return render(request, 'signup.html')
@login_required
def income_f(request):
    if request.method == 'POST':
        inc=request.POST.get('inc')
        income1=income.objects.create(user=request.user,inc=inc)
        income1.save()
        expenses = Daily.objects.all()
    # categories = []
        amounts=[]
    
        week = ['Mon', 'Tue', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun']
        for expense in expenses:
        # categories.append(expense.category)
            sum1 = expense.food + expense.transport + expense.entertain + expense.stationary + expense.misc
            amounts.append(sum1)
            print(sum1)
            data_json = json.dumps(amounts)
        expenses_m = Monthly.objects.get(id=3)
    # categories = []
        amounts_m=[]
        categories = ['Rent','Utilities','Personal Care','Communication','Health']
    #for exp in expenses_m:
        # categories.append(expense.category)
        #sum2 = exp.rent + exp.utilities + exp.personal_care + exp.communication + exp.health
        amounts_m.append(expenses_m.rent)
        amounts_m.append(expenses_m.utilities)
        amounts_m.append(expenses_m.personal_care)
        amounts_m.append(expenses_m.communication)
        amounts_m.append(expenses_m.health)
        total_e=[]
        data_json1 = json.dumps(amounts_m)
        inc1=income.objects.get(id=1)
        inc=inc1.inc
        sum2=0
        for x in amounts:
            sum2=sum2+x
        for kai in amounts_m:
            sum2=sum2+kai
        saving=inc-sum2
        total_e.append(inc)
        total_e.append(sum2)
        total_e.append(saving)

        data_json2 = json.dumps(total_e)
        return render(request,'income.html',{'data_json2':data_json2})
    return render(request, 'budget.html')

@login_required
def daily_exp(request):
    if request.method == 'POST':
        food = request.POST.get('food')
        transport = request.POST.get('transport')
        entertain = request.POST.get('entertain')
        stationary = request.POST.get('stationary')
        misc = request.POST.get('misc')
        
        daily = Daily.objects.create(user=request.user,food=food, transport=transport, entertain=entertain, stationary=stationary, misc=misc)
        daily.save()
        expenses = Daily.objects.all()
    # categories = []
        amounts=[]
    
        week = ['Mon', 'Tue', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun']
        for expense in expenses:
        # categories.append(expense.category)
            sum1 = expense.food + expense.transport + expense.entertain + expense.stationary + expense.misc
            amounts.append(sum1)
            print(sum1)
        data_json = json.dumps(amounts)

        return render(request,'daily.html',{'data_json':data_json})
    return render(request, 'budget.html')

@login_required
def monthly_exp(request):
    if request.method == 'POST':
        rent = request.POST.get('rent')
        utilities = request.POST.get('utilities')
        personal_care = request.POST.get('personal_care')
        communication = request.POST.get('communication')
        health = request.POST.get('health')
        
        
        monthly = Monthly.objects.create(user=request.user, rent=rent, utilities=utilities, personal_care=personal_care, communication=communication, health=health)
        monthly.save()
            # categories = []
        expenses_m = Monthly.objects.get(id=3)
        amounts_m=[]
        categories = ['Rent','Utilities','Personal Care','Communication','Health']
    #for exp in expenses_m:
        # categories.append(expense.category)
        #sum2 = exp.rent + exp.utilities + exp.personal_care + exp.communication + exp.health
        amounts_m.append(expenses_m.rent)
        amounts_m.append(expenses_m.utilities)
        amounts_m.append(expenses_m.personal_care)
        amounts_m.append(expenses_m.communication)  
        amounts_m.append(expenses_m.health)
        
        data_json1 = json.dumps(amounts_m)


        return render(request,'monthly.html',{'data_json1':data_json1})
    return render(request, 'budget.html')

def chart_view_daily(request):
    expenses = Daily.objects.all()
    # categories = []
    amounts=[]
    
    week = ['Mon', 'Tue', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun']
    for expense in expenses:
        # categories.append(expense.category)
        sum1 = expense.food + expense.transport + expense.entertain + expense.stationary + expense.misc
        amounts.append(sum1)
        print(sum1)
        data_json = json.dumps(amounts)
    expenses_m = Monthly.objects.get(id=3)
    # categories = []
    amounts_m=[]
    categories = ['Rent','Utilities','Personal Care','Communication','Health']
    #for exp in expenses_m:
        # categories.append(expense.category)
        #sum2 = exp.rent + exp.utilities + exp.personal_care + exp.communication + exp.health
    amounts_m.append(expenses_m.rent)
    amounts_m.append(expenses_m.utilities)
    amounts_m.append(expenses_m.personal_care)
    amounts_m.append(expenses_m.communication)
    amounts_m.append(expenses_m.health)
    total_e=[]
    data_json1 = json.dumps(amounts_m)
    inc1=income.objects.get(id=1)
    inc=inc1.inc
    sum2=0
    for x in amounts:
        sum2=sum2+x
    for kai in amounts_m:
        sum2=sum2+kai
    saving=inc-sum2
    total_e.append(inc)
    total_e.append(sum2)
    total_e.append(saving)

    data_json2 = json.dumps(total_e)
    context = {'data_json': data_json,'data_json1': data_json1,'data_json2': data_json2}
    # data = {
    #     'Week': week,
    #     'amounts': amounts,
    # }
    return render(request, 'index.html', context)

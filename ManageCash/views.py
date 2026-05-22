from django.shortcuts import render,redirect
from ManageCash.models import *
from ManageCash.forms import *
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.db.models import Sum


def registerpage(request):
    if request.method=='POST':
        regdata=RegisterForm(request.POST)
        if regdata.is_valid():
            regdata.save()
            return redirect('loginpage')
    
    regdata=RegisterForm()
    context={
        'regdata':regdata
    }
        
    return render(request,'registerpage.html',context)


def loginpage(request):
    if request.method=='POST':
        logdata=LoginForm(request,request.POST)
        if logdata.is_valid():
            user=logdata.get_user()
            login(request,user)
            return redirect('profilepage')
    
    logdata=LoginForm()
    context={
        'logdata':logdata
    }      
    return render(request,'loginpage.html',context)

@login_required
def logoutpage(request):
    logout(request)
    return redirect('loginpage')

@login_required
def dashboardpage(request):
    user=request.user
    
    total_cash=CashModel.objects.filter(
        user=user
    ).aggregate(added_cash=Sum('amount')) ['added_cash'] or 0
    
    
    total_expense=ExpenseModel.objects.filter(
        user=user
    ).aggregate(added_expense=Sum('amount')) ['added_expense'] or 0
    
    balance=total_cash - total_expense
    
    if total_cash==total_expense:
        status='You have no money'
    elif total_cash<total_expense:
        status='You are in Debth'
    else:
        status='You have sufficient balance'
        
    context={
        'total_cash':total_cash,
        'total_expense':total_expense,
        'balance':balance,
        'status':status,
    }
    return render(request,'dashboardpage.html',context)

@login_required
def profilepage(request):
    return render(request,'profilepage.html')

@login_required
def profileupdate(request):
    user=request.user
    try:
        profdata=ProfileModel.objects.get(user=user)
    except ProfileModel.DoesNotExist:
        profdata=None
        
    if request.method=='POST':
        data=ProfileForm(request.POST,request.FILES,instance=profdata)
        if data.is_valid():
            profdata=data.save(commit=False)
            profdata.user=request.user
            profdata.save()
            return redirect('profilepage')
        
    data=ProfileForm(instance=profdata)
    context={
        'data':data,
        'title':'Profile Update',
        'button':'Update',
    }
        
    return render(request,'baseForm.html',context)


@login_required
def transactionpage(request):
    user=request.user
    CashData=CashModel.objects.filter(user=user)
    ExpenseData=ExpenseModel.objects.filter(user=user)
    context={
        'CashData':CashData,
        'ExpenseData':ExpenseData
    }
    return render(request,'transactionpage.html',context)

@login_required
def AddCash(request):
    if request.method=='POST':
        data=CashForm(request.POST)
        if data.is_valid():
            cashdata=data.save(commit=False)
            cashdata.user=request.user
            cashdata.save()
            return redirect('transactionpage')
    
    data=CashForm()
    context={
        'data':data,
        'title':'Add Cash',
        'button':'Add',
    }
    return render(request,'baseForm.html',context)

@login_required
def CashEdit(request,id):
    cashedit=CashModel.objects.get(id=id)
    if request.method=='POST':
        data=CashForm(request.POST,instance=cashedit)
        if data.is_valid():
            data.save()
            return redirect('transactionpage')
    
    data=CashForm(instance=cashedit)
    context={
        'data':data,
        'title':'Edit Cash',
        'button':'Update',
    }
    return render(request,'baseForm.html',context)

@login_required
def CashDelete(request,id):
    CashModel.objects.get(id=id).delete()
    return redirect('transactionpage')


@login_required
def AddExpense(request):
    if request.method=='POST':
        data=ExpenseForm(request.POST)
        if data.is_valid():
            cashdata=data.save(commit=False)
            cashdata.user=request.user
            cashdata.save()
            return redirect('transactionpage')
    
    data=ExpenseForm()
    context={
        'data':data,
        'title':'Add Expense',
        'button':'Add',
    }
    return render(request,'baseForm.html',context)

@login_required
def ExpenseEdit(request,id):
    expedit=ExpenseModel.objects.get(id=id)
    if request.method=='POST':
        data=ExpenseForm(request.POST,instance=expedit)
        if data.is_valid():
            data.save()
            return redirect('transactionpage')
     
    data=ExpenseForm(instance=expedit)
    context={
        'data':data,
        'title':'Edit Expense',
        'button':'Update',
    }
    return render(request,'baseForm.html',context)

@login_required
def ExpenseDelete(request,id):
    ExpenseModel.objects.get(id=id).delete()
    return redirect('transactionpage')

from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import CurrentForm
from django.contrib import messages
import xlwt
from django.http import HttpResponse
from django.contrib.auth.models import User
from datetime import datetime, timezone


# Create your views here.

@login_required(login_url='account-login')
def index(request):
    comp_tasks_count = Current.objects.filter(status='Completed').count()
    del_tasks_count = Current.objects.filter(status='Deleted').count()
    curr_tasks_count = Current.objects.filter(status='Current').count()
    context = {
        'comp_tasks_count': comp_tasks_count,
        'del_tasks_count': del_tasks_count,
        'curr_tasks_count': curr_tasks_count,
    }
    return render(request, 'dash/index.html', context)


def about(request):
    
    return render(request, 'dash/about.html')

@login_required(login_url='account-login')
def current(request):
    curr_tasks = Current.objects.filter(status='Current')
    curr_tasks_count = curr_tasks.count()

    del_tasks_count = Current.objects.filter(status='Deleted').count()
    comp_tasks_count = Current.objects.filter(status='Completed').count()
   
    if request.method == "POST":
        form = CurrentForm(request.POST)
        if form.is_valid():
            form.save()
            task_name = form.cleaned_data.get('task')
            messages.success(request, f'{task_name} has been added')
            
            return redirect('dashboard-current')
    else:
        form = CurrentForm()

    context = {
        'comp_tasks_count': comp_tasks_count,
        'del_tasks_count': del_tasks_count,
        'curr_tasks': curr_tasks,
        'curr_tasks_count': curr_tasks_count,
        'form': form,
    }
    return render(request, 'dash/current.html', context)


@login_required(login_url='account-login')
def current_delete(request, pk):
    curr_del = Current.objects.get(id=pk)
    if request.method == "POST":
        curr_del.delete()
        return redirect('dashboard-current')

    return render(request, 'dash/current_delete.html')


@login_required(login_url='account-login')
def current_update(request, pk):
    curr_up = Current.objects.get(id=pk)
    if request.method == "POST":
        form = CurrentForm(request.POST, instance=curr_up)
        if form.is_valid():
            form.save()
            return redirect('dashboard-current')
    else:
        form = CurrentForm(instance=curr_up)
    context = {
        'form': form,
    }
    return render(request, 'dash/current_update.html', context)


@login_required(login_url='account-login')
def completed_delete(request, pk):
    comp_del = Current.objects.get(id=pk)
    if request.method == "POST":
        comp_del.delete()
        return redirect('dashboard-current')

    return render(request, 'dash/completed_delete.html')


@login_required(login_url='account-login')
def completed_update(request, pk):
    comp_up = Current.objects.get(id=pk)
    if request.method == "POST":
        form = CurrentForm(request.POST, instance=comp_up)
        if form.is_valid():
            form.save()
            return redirect('dashboard-current')
    else:
        form = CurrentForm(instance=comp_up)
    context = {
        'form': form,
    }
    return render(request, 'dash/completed_update.html', context)


@login_required(login_url='account-login')
def completed(request):
    comp_tasks = Current.objects.filter(status='Completed')
    comp_tasks_count = comp_tasks.count()

    del_tasks_count = Current.objects.filter(status='Deleted').count()
    curr_tasks_count = Current.objects.filter(status='Current').count()


    context = {
        'comp_tasks': comp_tasks,
        'comp_tasks_count': comp_tasks_count,
        'del_tasks_count': del_tasks_count,
        'curr_tasks_count': curr_tasks_count,
    }
    return render(request, 'dash/completed.html', context)


@login_required(login_url='account-login')
def deleted(request):
    del_tasks = Current.objects.filter(status='Deleted')
    del_tasks_count = del_tasks.count()
    comp_tasks_count = Current.objects.filter(status='Completed').count()
    curr_tasks_count = Current.objects.filter(status='Current').count()

    context = {
        'del_tasks': del_tasks,
        'comp_tasks_count': comp_tasks_count,
        'del_tasks_count': del_tasks_count,
        'curr_tasks_count': curr_tasks_count,
    }
    
    return render(request, 'dash/deleted.html', context)

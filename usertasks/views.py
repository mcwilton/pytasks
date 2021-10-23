from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import CurrentForm
from django.contrib import messages
from datetime import datetime, timezone


@login_required(login_url='account-login')
def index(request):
    current_tasks_count = Current.objects.filter(status='Current').count()
    completed_tasks_count = Current.objects.filter(status='Completed').count()
    deleted_tasks_count = Current.objects.filter(status='Deleted').count()
    
    context = {
        'deleted_tasks_count': deleted_tasks_count,
        'completed_tasks_count': completed_tasks_count,
        'current_tasks_count': current_tasks_count,
    }
    return render(request, 'dash/index.html', context)


@login_required(login_url='account-login')
def current(request):
    current_tasks = Current.objects.filter(status='Current')
    current_tasks_count = current_tasks_count.count()

    deleted_tasks_count = Current.objects.filter(status='Deleted').count()
    completed_tasks_count = Current.objects.filter(status='Completed').count()
   
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
        'completed_tasks_count': completed_tasks_count,
        'deleted_tasks_count': deleted_tasks_count,
        'current_tasks': current_tasks,
        'current_tasks_count': current_tasks_count,
        'form': form,
    }
    return render(request, 'dash/current.html', context)


@login_required(login_url='account-login')
def current_delete(request, pk):
    current_deleted = Current.objects.get(id=pk)
    if request.method == "POST":
        current_deleted.delete()
        return redirect('dashboard-current')

    return render(request, 'dash/current_delete.html')


@login_required(login_url='account-login')
def current_update(request, pk):
    current_updated = Current.objects.get(id=pk)
    if request.method == "POST":
        form = CurrentForm(request.POST, instance=current_updated)
        if form.is_valid():
            form.save()
            return redirect('dashboard-current')
    else:
        form = CurrentForm(instance=current_updated)
    context = {
        'form': form,
    }
    return render(request, 'dash/current_update.html', context)


@login_required(login_url='account-login')
def completed_delete(request, pk):
    completed_deleted = Current.objects.get(id=pk)
    if request.method == "POST":
        completed_deleted.delete()
        return redirect('dashboard-current')

    return render(request, 'dash/completed_delete.html')


@login_required(login_url='account-login')
def completed_update(request, pk):
    completed_updated = Current.objects.get(id=pk)
    if request.method == "POST":
        form = CurrentForm(request.POST, instance=completed_update)
        if form.is_valid():
            form.save()
            return redirect('dashboard-current')
    else:
        form = CurrentForm(instance=completed_update)
    context = {
        'form': form,
    }
    return render(request, 'dash/completed_update.html', context)


@login_required(login_url='account-login')
def completed(request):
    completed_tasks = Current.objects.filter(status='Completed')
    completed_tasks_count = completed_tasks.count()

    deleted_tasks_count = Current.objects.filter(status='Deleted').count()
    current_tasks_count = Current.objects.filter(status='Current').count()


    
    context = {
        'comp_tasks': comp_tasks,
        'completed_tasks_count': comp_tasks_count,
        'deleted_tasks_count': del_tasks_count,
        'current_tasks_count': curr_tasks_count,
    }
    return render(request, 'dash/completed.html', context)


@login_required(login_url='account-login')
def deleted(request):
    deleted_tasks = Current.objects.filter(status='Deleted')
    deleted_tasks_count = del_tasks.count()
    completed_tasks_count = Current.objects.filter(status='Completed').count()
    current_tasks_count = Current.objects.filter(status='Current').count()

    context = {
        'del_tasks': delete_tasks,
        'comp_tasks_count': complete_tasks_count,
        'del_tasks_count': delete_tasks_count,
        'curr_tasks_count': curr_tasks_count,
    }
    
    return render(request, 'dash/deleted.html', context)


def about(request):
    
    return render(request, 'dash/about.html')
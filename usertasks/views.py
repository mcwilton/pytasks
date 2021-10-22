# from django.shortcuts import redirect, render
# from .models import *
# from django.contrib.auth.decorators import login_required
# from .forms import CurrentForm
# from django.contrib import messages

# #import xlwt
# from django.http import HttpResponse
# from django.contrib.auth.models import User
# from datetime import datetime, timezone


# # Create your views here.

# @login_required(login_url='account-login')
# def index(request):
#     completed_tasks_count = Current.objects.filter(status='Completed').count()
#     deleted_tasks_count = Current.objects.filter(status='Deleted').count()
#     current_tasks_count = Current.objects.filter(status='Current').count()
#     context = {
#         'completed_tasks_count': completed_tasks_count,
#         'deleted_tasks_count': deleted_tasks_count,
#         'current_tasks_count': current_tasks_count,
#     }
#     return render(request, 'task/dashboard/index.html', context)


# def about(request):
    
#     return render(request, 'tasks/dashboard/about.html')

# @login_required(login_url='account-login')
# def current(request):
#     curr_tasks = Current.objects.filter(status='Current')
#     curr_tasks_count = curr_tasks.count()

#     del_tasks_count = Current.objects.filter(status='Deleted').count()
#     comp_tasks_count = Current.objects.filter(status='Completed').count()
   
#     if request.method == "POST":
#         form = CurrentForm(request.POST)
#         if form.is_valid():
#             form.save()
#             task_name = form.cleaned_data.get('task')
#             messages.success(request, f'{task_name} has been added')
            
#             return redirect('dashboard-current')
#     else:
#         form = CurrentForm()

#     context = {
#         'comp_tasks_count': comp_tasks_count,
#         'del_tasks_count': del_tasks_count,
#         'curr_tasks': curr_tasks,
#         'curr_tasks_count': curr_tasks_count,
#         'form': form,
#     }
#     return render(request, 'task/dashboard/current.html', context)


# @login_required(login_url='account-login')
# def current_delete(request, pk):
#     curr_del = Current.objects.get(id=pk)
#     if request.method == "POST":
#         curr_del.delete()
#         return redirect('dashboard-current')

#     return render(request, 'task/dashboard/current_delete.html')


# @login_required(login_url='account-login')
# def current_update(request, pk):
#     curr_up = Current.objects.get(id=pk)
#     if request.method == "POST":
#         form = CurrentForm(request.POST, instance=curr_up)
#         if form.is_valid():
#             form.save()
#             return redirect('dashboard-current')
#     else:
#         form = CurrentForm(instance=curr_up)
#     context = {
#         'form': form,
#     }
#     return render(request, 'task/dashboard/current_update.html', context)


# @login_required(login_url='account-login')
# def completed_delete(request, pk):
#     comp_del = Current.objects.get(id=pk)
#     if request.method == "POST":
#         comp_del.delete()
#         return redirect('dashboard-current')

#     return render(request, 'task/dashboard/completed_delete.html')


# @login_required(login_url='account-login')
# def completed_update(request, pk):
#     comp_up = Current.objects.get(id=pk)
#     if request.method == "POST":
#         form = CurrentForm(request.POST, instance=comp_up)
#         if form.is_valid():
#             form.save()
#             return redirect('dashboard-current')
#     else:
#         form = CurrentForm(instance=comp_up)
#     context = {
#         'form': form,
#     }
#     return render(request, 'task/dashboard/completed_update.html', context)


# @login_required(login_url='account-login')
# def completed(request):
#     comp_tasks = Current.objects.filter(status='Completed')
#     comp_tasks_count = comp_tasks.count()

#     del_tasks_count = Current.objects.filter(status='Deleted').count()
#     curr_tasks_count = Current.objects.filter(status='Current').count()


    
#     context = {
#         'comp_tasks': comp_tasks,
#         'comp_tasks_count': comp_tasks_count,
#         'del_tasks_count': del_tasks_count,
#         'curr_tasks_count': curr_tasks_count,
#     }
#     return render(request, 'task/dashboard/completed.html', context)


# @login_required(login_url='account-login')
# def deleted(request):
#     del_tasks = Current.objects.filter(status='Deleted')
#     del_tasks_count = del_tasks.count()
#     comp_tasks_count = Current.objects.filter(status='Completed').count()
#     curr_tasks_count = Current.objects.filter(status='Current').count()

#     context = {
#         'del_tasks': del_tasks,
#         'comp_tasks_count': comp_tasks_count,
#         'del_tasks_count': del_tasks_count,
#         'curr_tasks_count': curr_tasks_count,
#     }
    
#     return render(request, 'task/dashboard/deleted.html', context)


# @login_required(login_url='account-login')
# def export_excel(request, id):
#     if id == 1: # current
#         obj = Current
#         obj_name = 'Current'
#     elif id == 2: # completed
#         obj = Completed
#         obj_name = 'Completed'
#     elif id == 3: # Deleted
#         obj = Deleted
#         obj_name = 'Deleted'
#     else:
#         print('no id')

    
#     response=HttpResponse(content_type='application/ms-excel')
#     response['Content-Disposition'] = f'attachment; filename={obj_name}.xls' 
  
#     wb = xlwt.Workbook(encoding='utf-8')
#     ws = wb.add_sheet(f'{obj_name} Tasks')
#     row_num = 0

#     font_style = xlwt.XFStyle()
#     font_style.font.bold = True

#     columns = ['task', 'user', 'date', 'status']

#     for col_num in range(len(columns)):
#         ws.write(row_num, col_num, columns[col_num], font_style) # at 0 row 0 column 

#     curr_tasks = Current.objects.filter(status=f'{obj_name}').values_list('task', 'user', 'date', 'status')
    
#     for row in curr_tasks:
#         row_num += 1
#         for col_num in range(len(row)):
#             ws.write(row_num, col_num, row[col_num])
        
#     wb.save(response)
#     return response

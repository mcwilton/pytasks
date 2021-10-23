from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.index, name='index'),
    path('about/', views.about, name='dashboard-about'),
    path('current/', views.current, name='dashboard-current'),
    path('current_delete/<int:pk>/', views.current_delete, name='dashboard-current-delete'),
    path('current_update/<int:pk>/', views.current_update, name='dashboard-current-update'),
    path('completed_delete/<int:pk>/', views.completed_delete, name='dashboard-completed-delete'),
    path('completed_update/<int:pk>/', views.completed_update, name='dashboard-completed-update'),
    path('completed/', views.completed, name='dashboard-completed'),
    path('deleted/', views.deleted, name='dashboard-deleted'),
]

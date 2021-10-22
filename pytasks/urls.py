"""pytasks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from users import views as users_view
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from users import views

#app_name = 'task'

urlpatterns = [
    path('admin/', admin.site.urls),

    #path('', include('tasks.urls')),

    path('register/', users_view.register, name='account-register'),
    path('profile/', users_view.profile, name='account-profile'),
    path('profile-update/', users_view.profile_update, name='account-profile-update'),
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='account-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='account-logout'),

   # path('export_excel/<int:id>/', views.export_excel, name='export_excel'),

    path('password_reset/', PasswordResetView.as_view(template_name='reset_password_form.html'), name='password-reset'),
    path('password_reset_done/', PasswordResetDoneView.as_view(template_name='reset_password_done.html'), name='password-reset-done'),
    path('password_reset_confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='reset_papssword_confirm.html'), name='password-reset-confirm'),
    path('password_complete/', PasswordResetCompleteView.as_view(template_name='reset_password_email.html'), name='password-change'),
   
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
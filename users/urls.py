   
from django.contrib.auth import views
from django.urls import path

from django.conf.urls.static import static

from users import views as users_view
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from users import views

urlpatterns = [
   path('register/', users_view.register, name='account-register'),
   path('profile/', users_view.profile, name='account-profile'), 
   path('profile-update/', users_view.profile_update, name='account-profile-update'),
   path('', auth_views.LoginView.as_view(template_name='login.html'), name='account-login'),
   path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='account-logout'),
   path('password_reset/', PasswordResetView.as_view(template_name='password_reset_form.html'), name='password-reset'),
   path('password_reset_done/', PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password-reset-done'),
   path('password_reset_confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password-reset-confirm'),
   path('password_complete/', PasswordResetCompleteView.as_view(template_name='password_reset_email.html'), name='password-change'),
   ]
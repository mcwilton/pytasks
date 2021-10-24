from .forms import CreateUserForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

def register(request):
    if request.method == 'POST':   
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Bravo, {username} account created. \nPlease Login')
            return redirect('account-login')
    else:
        form = CreateUserForm()
       
    context = {
        'form': form
    }
    return render(request, 'register.html', context)

@login_required
def profile(request):
    return render(request, 'profile.html')


def profile_update(request):
    if request.method == 'POST':
        userform = UserUpdateForm(request.POST, instance=request.user)
        profileform = UserUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            profileform.save()
            return redirect('account-profile')
    else:
        userform = UserUpdateForm(instance=request.user)
        profileform = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'userform': userform,
        'profileform': profileform,
    }
    return render(request, 'profile_update.html', context)

                
def loginPage(request):
    return render(request, 'login.html')



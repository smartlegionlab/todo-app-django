from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from profiles.forms import ProfileSettingsForm, ProfilePasswordChangeForm, SignUpForm
from profiles.models import Profile


@login_required
def user_profile(request):
    return render(request, 'profiles/profile.html')


def login_view(request):
    if request.user.is_authenticated:
        return redirect('profiles:profile')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not email or not password:
            messages.error(request, 'Email and password are required.')
            return render(request, 'profiles/login.html')

        user = authenticate(request, email=email, password=password)
        profile = Profile.objects.filter(email=email).first()

        if profile:
            if not profile.is_active:
                messages.error(request, 'Account is not active.')
                return redirect('profiles:login')

        if user is not None:
            login(request, user)
            messages.success(request, f'{user.full_name}. Welcome to the - Smart ToDo App.')
            return redirect('core:index')
        else:
            messages.error(request, 'Account not found.')
            return render(request, 'profiles/login.html')
    return render(request, 'profiles/login.html')


def logout_view(request):
    logout(request)
    return redirect('profiles:login')


@login_required
def profile_settings(request):
    profile = Profile.objects.get(pk=request.user.id)
    form = ProfileSettingsForm(request.POST or None, instance=profile)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated.')
            return redirect('profiles:profile')
    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'profiles/profile_settings.html', context)


@login_required
def change_password(request):
    if request.method == 'POST':
        form = ProfilePasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('profiles:profile')
    else:
        form = ProfilePasswordChangeForm(user=request.user)
    context = {
        'form': form
    }
    return render(request, 'profiles/change_password.html', context)


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, 'Your account has been created.')
            return redirect('profiles:login')
        else:
            messages.error(request, 'Error! User like this E-mail already registered in system!')
    else:
        form = SignUpForm()

    context = {
        'form': form,
    }

    return render(request, 'profiles/register.html', context)

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from profiles.models import Profile


@login_required
def user_profile(request):
    message = request.session.pop('message', None)
    context = {
        'message': message,
    }
    return render(request, 'profiles/profile.html', context)


def login_view(request):
    message = request.session.pop('message', None)

    if request.user.is_authenticated:
        return redirect('profiles:profile')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not email or not password:
            message = {
                'type': 'danger',
                'text': 'Email and password are required.',
            }
            return render(request, 'profiles/login.html', {'message': message})

        user = authenticate(request, email=email, password=password)
        profile = Profile.objects.filter(email=email).first()

        if profile:
            if not profile.is_active:
                msg = f'Your account is blocked! To unblock, contact the administrator.'
                message = {
                    'type': 'danger',
                    'text': msg
                }
                request.session['message'] = message
                return redirect('profiles:login')

        if user is not None:
            login(request, user)
            message = {
                'type': 'success',
                'text': f'{user.full_name}. Welcome to the - Smart ToDo App.'
            }
            request.session['message'] = message
            return redirect('core:index')
        else:
            message = {
                'type': 'danger',
                'text': 'Incorrect email or password',
            }
            return render(request, 'profiles/login.html', {'message': message})

    context = {
        'message': message
    }
    return render(request, 'profiles/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('profiles:login')

from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def user_profile(request):
    message = request.session.pop('message', None)
    context = {
        'message': message,
    }
    return render(request, 'profiles/profile.html', context)

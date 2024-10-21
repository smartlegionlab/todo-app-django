from django.shortcuts import render


def index(request):
    message = request.session.pop('message', None)
    return render(request, 'core/index.html', {'message': message})

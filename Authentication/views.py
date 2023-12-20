from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required


def login_user(request):
    """
    This method validate the user and login
    :param request: Type of request (GET or POST)
    :return: Login page
    """
    if request.method == 'POST':
        request.session['username'] = request.POST.get('username')
        password = request.POST.get('password')
        username = request.session.get('username')
        request.session['username'] = username
        user = authenticate(request, username=username, password=password)

        if user is None:
            context = {
                'text': 'Invalid Username or Password'
            }
            messages.success(request, 'Invalid Username or Password')
            return render(request, 'login.html', context)

        else:
            context = {'username': username}
            login(request, user)
            return render(request, 'index.html', context)
    else:
        context = {}
        return render(request, 'index.html', context)


def login_get(request):
    """
    This method logout the user
    :param request: Type of request (GET or POST)
    :return: Logout page
    """
    return render(request, 'login.html')


@login_required
def logout_user(request):
    """
    This method logout the user
    :param request: Type of request (GET or POST)
    :return: Logout page
    """
    logout(request)
    return render(request, 'logout.html')

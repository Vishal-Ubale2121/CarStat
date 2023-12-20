from django.shortcuts import render

# Create your views here.


def dealer_registration(request):
    """
    This method logout the user
    :param request: Type of request (GET or POST)
    :return: Logout page
    """
    return render(request, 'dealer_registration.html')
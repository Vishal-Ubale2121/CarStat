from django.urls import path
from . import views as authentication_views
from Screens import views as screen_views

urlpatterns = [
    path('', authentication_views.login_user, name='login'),
    path('logout', authentication_views.logout_user, name='logout'),
    path('login', authentication_views.login_get, name='login_get'),
    path('dealer_registration', screen_views.dealer_registration, name='dealer_registration'),
]
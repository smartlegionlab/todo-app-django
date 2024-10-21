from django.urls import path

from . import views

app_name = 'profiles'

urlpatterns = [
    path('', views.user_profile, name='profile'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('settings/', views.profile_settings, name='profile_settings'),
    path('change-password/', views.change_password, name='change_password'),
]

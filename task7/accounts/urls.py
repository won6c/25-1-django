from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.login_view ,name='logout')
]
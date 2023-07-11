from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [
    path('', views.index, name = 'index'),
    # Authentication urls
    path('login/', views.login_request, name = 'login'),
    path('logout/', views.logout_request, name = 'logout'),
    path('register/', views.register_request, name = 'register'),
]

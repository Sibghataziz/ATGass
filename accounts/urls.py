from django.urls import path
from .views import register_view
from django.contrib.auth import views

urlpatterns = [
    path('register/', register_view, name="register"),
    # path('', home_view, name ='home'),
     path('login/', views.LoginView.as_view(template_name='accounts/login.html'), name="login"),
    path('logout/', views.LogoutView.as_view(template_name='accounts/logout.html'), name="logout"),
]

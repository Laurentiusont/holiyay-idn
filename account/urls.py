from django.urls import path
from .views import loginView, logoutView,registerPage
app_name = 'account'
urlpatterns = [
    path('login',  loginView, name="login"),
    path('logout',  logoutView, name="logout"),
    path('register',  registerPage, name="register"),
]

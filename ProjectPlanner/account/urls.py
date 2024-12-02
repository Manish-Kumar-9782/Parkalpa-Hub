from django.urls import path
from .views import login_account, register_account, logout

urlpatterns = [
    path("login", view=login_account, name="login"),
    path("register", view=register_account, name="register"),
    path("logout", view=logout, name="logout"),

]

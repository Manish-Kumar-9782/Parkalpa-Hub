from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from ProjectPlanner.Utility.error import Error
# Create your views here.


def login_account(request):

    errors = Error()

    login_page = "account/login.html"

    if request.method == "GET":

        if not request.user.is_authenticated:
            return render(request, login_page)

        return redirect("home")

    if request.method == "POST":

        data = request.POST
        username = data.get('username')
        password = data.get('password')

        user = authenticate(request,  username=username, password=password)

        if not user:
            errors.add_error("login_error", "Invalid username or password")
            return render(request, login_page, {"errors": errors.get_errors()})

        auth.login(request, user)
        return redirect("home")


def register_account(request):

    error = Error()

    if request.method == "GET":

        return render(request, "account/register.html")

    if request.method == "POST":
        data = request.POST

        username = data.get("username")
        firstname = data.get("firstname")
        lastname = data.get("lastname")
        email = data.get("email")
        password = data.get("password")
        c_password = data.get("c_password")

        # for now we are not doing any validation on the from's data.
        # leaving it for future update.

        if password != c_password:
            error.add_error("password_mismatch",
                            "Password  do not match, please  try again")
            return render(request, "account/login.html", {"errors": error})

        # if password and confirm password are matched then we need to save the user data.
        user = User.objects.create_user(username=username, email=email, password=password, first_name=firstname,
                                        last_name=lastname)
        user.save()

        return redirect("login")


def logout(request):
    auth.logout(request)
    return redirect("home")

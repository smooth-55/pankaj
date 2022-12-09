from django.shortcuts import redirect, render
from user.forms import UserForm
from django.views import View
from django.contrib.auth.models import auth
from django.contrib import messages
from django.db import transaction
from django.contrib import messages


# Create your views here.


class Login(View):
    def get(self, request):
        return render(request, "user/login.html")

    def post(self, request):
        context = dict()
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth.login(request, user)
                return redirect("home")
            context["err"] = "Invalid Credentials"
            messages.error(request, "Invalid Credentials")
            return render(request, "user/login.html", context)
        context["err"] = "Invalid Credentials"
        messages.error(request, "Invalid Credentials")
        return render(request, "user/login.html", context)


class Register(View):
    def get(self, request):

        user_form = UserForm()

        context = {"user_form": user_form}
        print(user_form)
        return render(request, "user/register.html", context)

    @transaction.atomic
    def post(self, request):
        context = dict()
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            messages.success(
                request,
                "Registration success",
            )
            return redirect("login")
        else:
            _err = user_form.errors.as_json()
            if request.POST["password2"] == user_form.cleaned_data.get("password1"):
                if "password2" in _err:
                    context["password_err"] = "This password is too common."
            else:
                context["not_match"] = "Both password should be same."
            if "username" in _err:
                context["uq_username"] = "Username already exists."
        context["user_form"] = user_form
        return render(request, "user/register.html", context)


class Logout(View):
    def get(self, request):
        auth.logout(request)
        return redirect("login")

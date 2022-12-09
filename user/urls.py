from django.urls import path
from user.views import Login, Register, Logout

urlpatterns = [
    path("register/", Register.as_view(), name="register"),
    path("logout/", Logout.as_view(), name="logout"),
]

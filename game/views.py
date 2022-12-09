from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class HomeView(LoginRequiredMixin, TemplateView):
    login_url = "/login"
    template_name = "game/home.html"

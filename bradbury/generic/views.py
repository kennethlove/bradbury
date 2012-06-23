from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, RedirectView, FormView

from braces.views import LoginRequiredMixin

from generic.forms import SimpleAddForm, LoginForm

class HomepageView(TemplateView):
    template_name = "generic/index.html"

    def get_context_data(self, **kwargs):
        kwargs = super(HomepageView, self).get_context_data(**kwargs)
        kwargs.update({"simple_add_form": SimpleAddForm()})
        return kwargs


class LoginView(FormView):
    form_class = LoginForm
    template_name = "generic/login.html"

    def form_valid(self, form):
        user = authenticate(username=form.cleaned_data["username"],
            password=form.cleaned_data["password"])

        if user is not None:
            login(self.request, user)
            return HttpResponseRedirect(reverse("generic:homepage"))
        return HttpResponseRedirect(reverse("generic:login"))

class LogoutView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self, **kwargs):
        return reverse("generic:homepage")

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)

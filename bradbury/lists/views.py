from django.core.urlresolvers import reverse
from django.views.generic import CreateView, DetailView

from braces.views import LoginRequiredMixin

from lists.forms import ListForm
from lists.models import List


class SimpleListCreateView(LoginRequiredMixin, CreateView):
    form_class = ListForm
    model = List
    template_name = "lists/form.html"

    def get_success_url(self):
        return reverse("lists:detail", kwargs={"pk": self.object.pk})

    def post(self, request, *args, **kwargs):
        form = ListForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

class ListDetailView(DetailView):
    model = List
    template_name = "lists/detail.html"

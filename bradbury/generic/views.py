from django.views.generic import TemplateView

from generic.forms import SimpleAddForm

class HomepageView(TemplateView):
    template_name = "generic/index.html"

    def get_context_data(self, **kwargs):
        kwargs = super(HomepageView, self).get_context_data(**kwargs)
        kwargs.update({"simple_add_form": SimpleAddForm()})
        return kwargs

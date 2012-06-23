import floppyforms as forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field
from crispy_forms.bootstrap import FormActions

class SimpleAddForm(forms.Form):
    search = forms.CharField()

    def __init__(self, *args, **kwargs):
        super(SimpleAddForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper
        self.helper.form_method = "POST"
        self.helper.form_class = "form-search"
        self.helper.layout = Layout(
            Field("search", css_class="search-query"),
            FormActions(
                Submit('', "Search", css_class="btn-primary")
            )
        )

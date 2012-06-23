from django.contrib.auth import authenticate
from django.contrib.auth.models import User

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

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(
        widget=forms.PasswordInput()
    )

    error_messages = {
        "invalid_login": "Please enter a correct email address and password. "
            "Note that both fields are case-sensitive.",
        "no_cookies": "Your Web browser doesn't appear to have cookies "
            "enabled. Cookies are required for logging in.",
        "inactive": "This account hasn't been activated. Have you checked your"
            "email, including spam folders, for an activation email?",
    }

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        if email and password:
            try:
                username_user = User.objects.get(email=email)
            except User.DoesNotExist:
                raise forms.ValidationError(
                    self.error_messages["invalid_login"])

            self.user_cache = authenticate(username=username_user.username,
                password=password)

            if self.user_cache is None:
                raise forms.ValidationError(
                    self.error_messages["invalid_login"])
            elif not self.user_cache.is_active:
                raise forms.ValidationError(
                    self.error_messages["inactive"])
            self.check_for_test_cookie()

            self.cleaned_data["username"] = self.user_cache.username

            return self.cleaned_data

    def check_for_test_cookie(self):
        if self.request and not self.request.session.test_cookie_worked():
            raise forms.ValidationError(self.error_messages["no_cookies"])

    def get_user_id(self):
        if self.user_cache:
            return self.user_cache.id
        return None

    def get_user(self):
        return self.user_cache

    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        self.user_cache = None
        super(LoginForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = "POST"
        self.helper.form_class = "form-horizontal"
        self.helper.layout = Layout(
            "email",
            "password",
            FormActions(
                Submit('', "Log in", css_class="btn-primary")
            )
        )

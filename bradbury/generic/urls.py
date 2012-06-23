from django.conf.urls import patterns, url

from generic.views import HomepageView, LoginView, LogoutView

urlpatterns = patterns('',
    url(r"^accounts/login/$", LoginView.as_view(), name="login"),
    url(r"^accounts/logout/$", LogoutView.as_view(), name="logout"),
    url(r"^$", HomepageView.as_view(), name="homepage"),
)

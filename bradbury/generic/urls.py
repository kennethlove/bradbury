from django.conf.urls import patterns, url

from generic.views import HomepageView

urlpatterns = patterns('',
    url("^$", HomepageView.as_view(), name="homepage"),
)

from django.conf.urls import patterns, url

from lists.views import SimpleListCreateView, ListDetailView

urlpatterns = patterns('',
    url("^create/simple/$", SimpleListCreateView.as_view(),
        name="simple_create"),
    url("^detail/(?P<pk>\d+)/$", ListDetailView.as_view(),
        name="detail"),
)

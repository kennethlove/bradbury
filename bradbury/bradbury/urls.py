from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r"^admin/", include(admin.site.urls)),
    (r"^accounts/", include("userena.urls")),

    (r"^lists/", include("lists.urls", namespace="lists")),
    (r"", include("generic.urls", namespace="generic")),
)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()

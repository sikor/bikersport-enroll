from allauth.account import views
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^', include('enrollapp.urls')),
                       url('^social/', include('allauth.socialaccount.urls')),
                       url('^fb/', include('allauth.socialaccount.providers.facebook.urls')),
                       url(r"^logout/$", views.logout, name="account_logout"),
)

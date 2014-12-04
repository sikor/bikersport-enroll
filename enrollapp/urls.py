from django.conf.urls import patterns, url
from enrollapp import views

__author__ = 'pawel'

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'enroll.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^event/(\w+)$', views.event, name="event"),
                       url(r'^enroll/(\w+)$', views.enroll_user, name="enroll"),
                       url(r'^unenroll/(\w+)$', views.unenroll, name="unenroll"),
                       url(r'^user_details/(\w+)$', views.user_details, name="user_details"),
                       url(r'^$', views.index, name="index")
)


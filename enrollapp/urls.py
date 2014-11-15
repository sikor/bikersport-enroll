from django.conf.urls import patterns, url
from enrollapp import views

__author__ = 'pawel'

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'enroll.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^event/(\w+)$', views.event, name="event"),
                       url(r'^$', views.index, name="index")
)


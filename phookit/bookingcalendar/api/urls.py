from django.conf.urls import patterns, url
from phookit.bookingcalendar.api import views

urlpatterns = patterns('',
    url(r'^feed/$', views.BookingList.as_view(), name='calendar-list'),
    url(r'^admin/(?P<pk>[0-9]+)/$', views.BookingAdminDetail.as_view()),
    url(r'^admin/$', views.BookingAdminList.as_view(), name='calendar-admin-list'),
)

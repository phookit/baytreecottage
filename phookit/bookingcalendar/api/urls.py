from django.conf.urls import patterns, url
from phookit.bookingcalendar.api import views

urlpatterns = patterns('',
    url(r'^feed/$', views.CalendarItemList.as_view(), name='calendar-list'),
    url(r'^feed/(?P<pk>[0-9]+)/$', views.CalendarItemDetail.as_view()),
)

from django.conf.urls import patterns, include, url
from phookit.bookingcalendar import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='calendar-index'),
)

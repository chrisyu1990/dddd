from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^beacons/$', views.beacon_list, name='beacon_list'),
    url(r'^sessions/$', views.session_list, name='session_list'),
    url(r'^add/attendee/new$', views.post_new_attendee, name='post_new_attendee'),
]

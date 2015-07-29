from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^clubs/$', views.club_list, name="club_list"),
    url(r'^clubs/(?P<pk>[0-9]+)/$', views.ClubDetail.as_view(), name="club_detail"),
]
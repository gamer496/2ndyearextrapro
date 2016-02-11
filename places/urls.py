from django.conf.urls import url
from places import views

urlpatterns=[
    url(r'^$',views.index,name="placeshome"),
    url(r'^addplace',views.addplace,name="addplace"),
    url(r'^viewplaces',views.viewplaces,name="viewplaces"),
    url(r'^viewplace/(?P<id>\d+)/$',views.viewplace,name="viewplace"),
    url(r'^viewplace/placevote',views.placevote,name="voteforplace"),
]

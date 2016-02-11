from django.conf.urls import url,include
from points import views

urlpatterns=[
    url(r'^$',views.index,name="pointshome"),
    url('addpoint/(?P<place_id>\d+)/$',views.addpoint,name="addpoint"),
    url('pointvote/(?P<point_id>\d+)/$',views.handlepointvote,name="voteforpoint"),
]

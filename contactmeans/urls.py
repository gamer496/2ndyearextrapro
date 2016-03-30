from django.conf.urls import url,include
from contactmeans.models import Messages
from contactmeans import views

urlpatterns=[
    url(r'^$',views.index,name="messageshome"),
    url(r'^sendmessage/(?P<receiver_id>.+)$',views.SendMessage,name="sendmessage"),
    url(r'^viewsentmessages',views.viewsentmessages,name="viewsentmessages"),
    url(r'^viewreceivedmessages',views.viewreceivedmessages,name="viewreceivedmessages"),
    url(r'^messagesent',views.messagesent,name="messagesent"),
]

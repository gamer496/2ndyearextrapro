from django.conf.urls import url
from wusers import views

urlpatterns=[
    url(r'^$',views.index,name="wusershome"),
    url(r'^registration',views.registration,name="userregistration"),
    url(r'^activate/(?P<key>.+)$',views.activation,name='useractivation'),
    url(r'^new_activation_link/(?P<user_id>\d+)/$',views.new_activation_link,name="useranotheractivation"),
    url(r'^login',views.wuser_login,name="userlogin"),
    url(r'^logout',views.wuser_logout,name="userlogout"),
    url(r'^resetpassword',views.reset,name="userpasswordreset"),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.reset_confirm, name='password_reset_confirm'),
    url(r'^successrequest',views.succeessrequest,name="successrequest"),
    url(r'^success',views.success,name="success"),
    url(r'^viewprofile/(?P<wuser_id>\d+)/$',views.viewprofile,name="viewprofile"),
]

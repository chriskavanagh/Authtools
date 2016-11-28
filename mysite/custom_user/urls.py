from django.conf.urls import url, include
from . import views



urlpatterns = [

    url(r'^register/$', views.register_user, name='register'),
    url(r'^register-done/$', views.register_done, name ='register_done'),
    url(r'^login/$', views.login_view, name='login'),
    
    url(r'^loggedin/$', views.logged_in, name='loggedin'),
    url(r'^loggedout/$', views.logout_view, name='loggedout'),
    
    url(r'^send-email/$', views.send_email, name='send_email'),
    url(r'^test_email_confirm/(?P<uuid64>[0-9A-Za-z]+)-(?P<token>.+)/$', views.test_email_confirm, name='confirm'),
    # ^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$
]

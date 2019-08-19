from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.users, name='users'),
    url(r'^/test_csrf$', views.test_csrf),
    url(r'^/test_csrf_server$', views.test_csrf_server),
    url(r'^/test_xss$', views.test_xss),
]
from django.conf.urls import url
from views import *


urlpatterns = [
    url(r'^$',  IndexView.as_view(), name='index'),
    url(r'^dashboard$',  DashboardView.as_view(), name='dashboard'),
]

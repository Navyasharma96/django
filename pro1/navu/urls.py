from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include

from.views import home_view,registratio_view,about_view,university_view,courses_view,login_view,registrationcarry_view,test


urlpatterns=[
    url(r'^$',home_view),
    url(r'^home',home_view),
    url(r'^reg',registratio_view),
    url(r'^regist',test),
    url(r'^bio',registrationcarry_view),
    url(r'^about',about_view),
    url(r'^university',university_view),
    url(r'^courses',courses_view),
    url(r'^login',login_view)

]
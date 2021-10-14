"""
前台首页url
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rango import views

urlpatterns = [
    path('',views.index),  # 首页url
	path(r'^category/(?P<category_name_slug>[\w\-]+)/$',
        views.show_category, name='show_category'),
    path(r'^accounts/', include('registration.backends.simple.urls'))
]

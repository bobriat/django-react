from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.PageList.as_view(), name='page-list'),
]

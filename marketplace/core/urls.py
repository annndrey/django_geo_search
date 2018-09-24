from django.conf.urls import url
from .views import (
	ActivitiesListView,
	ActivityDetailView,
	UpdateActivityView,
	ActivityRatingAjaxView,
	)
from core.models import models


app_name = 'core'

urlpatterns = [
   url(r'^$',ActivitiesListView.as_view(), name='list'),
   url(r"^(?P<slug>[\w-]+)/", ActivityDetailView.as_view(),name='detail_slug'),
   url(r'^(?P<pk>\d+)/', ActivityDetailView.as_view(), name='detail'),
   url(r'^(?P<slug>[\w-]+)/edit/', UpdateActivityView.as_view(),name='update_slug'),
   url(r'^(?P<pk>\d+)/edit/', UpdateActivityView.as_view(), name='update'),
   url(r'^ajax/rating/$',ActivityRatingAjaxView.as_view(), name='ajax_rating'),
   #url(r'^activities/(?P<slug>[\w-]+)/$', ActivityDetailView.as_view(), name='activity_slug_view'),
]


#url(r"^posts/in/(?P<slug>[-\w]+)/$",views.SingleGroup.as_view(),name="single"),

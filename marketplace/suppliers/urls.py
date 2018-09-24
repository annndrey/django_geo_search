from django.conf.urls import include, url
from django.contrib import admin
from core.views import (
	SuppliersActivitiesListView,
	CreateActivityView,
	UpdateActivityView
	)

from .views import (
	SupplierActivityDetailRedirectView, 
	SupplierDashboard
	)
from .models import SupplierAccount


app_name = 'suppliers'

urlpatterns = [
    url(r'^$', SupplierDashboard.as_view(), name='dashboard'),
    url(r'^activities/$',SuppliersActivitiesListView.as_view(), name='activities_list'),
    url(r'^activities/add/$',CreateActivityView.as_view(), name='activity_create'),
    url(r'^activities/(?P<pk>\d+)/edit/$', UpdateActivityView.as_view(), name='activity_edit'),
    url(r'^activities/(?P<pk>\d+)/$', SupplierActivityDetailRedirectView.as_view()),
] 
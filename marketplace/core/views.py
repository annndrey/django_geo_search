import os

from mimetypes import guess_type

from django.conf import settings
from wsgiref.util import FileWrapper

from django.db.models import Q

from django.views.generic import CreateView, ListView, DetailView
from django.shortcuts import render, Http404, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.urls import reverse
from suppliers.mixins import (
							SupplierAccountMixin
							)
from New.mixins import (
			MultiSlugMixin,
			SubmitBtnMixin,
			AjaxRequiredMixin,
			)
from .mixins import ProductManagerMixin
from django.views.generic import View
from core.models import Activity, Category, ActivityRating, MyActivities
from core.forms import ActivityAddForm
from Accounts.models import User
from New.mixins import (
	LoginRequiredMixin
	)

# Create your views here.


class ActivityRatingAjaxView(AjaxRequiredMixin, View):
	def post(self, request, *args, **kwargs):
		if not request.user.is_authenticated():
			return JsonResponse({}, status=401)
		# credit card required ** 
		
		user = request.user
		activity_id = request.POST.get("activity_id")
		rating_value = request.POST.get("rating_value")
		exists = Activity.objects.filter(id=activity_id).exists()
		if not exists:
			return JsonResponse({}, status=404)

		try:
			activity_obj = Activity.objects.get(id=activity_id)
		except:
			activity_obj = Activity.objects.filter(id=activity_id).first()

		rating_obj, rating_obj_created = ActivityRating.objects.get_or_create(
				user=user, 
				activity=activity_obj
				)
		try:
			rating_obj = ActivityRating.objects.get(user=user, activity=activity_obj)
		except ActivityRating.MultipleObjectsReturned:
			rating_obj = ActivityRating.objects.filter(user=user, activity=activity_obj).first()
		except:
			#rating_obj = ProductRating.objects.create(user=user, product=product_obj)
			rating_obj = ActivityRating()
			rating_obj.user = user
			rating_obj.activity = activity_obj
		rating_obj.rating = int(rating_value)
		# myactivities = user.myactivities.activities.all()

		# if activity_obj in myactivities:
		# 	rating_obj.verified = True
		# # verify ownership
		# rating_obj.save()

		# data = {
		# 	"success": True
		# }
		return JsonResponse(data)


class CreateActivityView(SupplierAccountMixin, SubmitBtnMixin, MultiSlugMixin, CreateView):
	model = Activity
	template_name = "activities/form.html"
	form_class = ActivityAddForm
	# success_url = "activities/"
	submit_btn = "Add Activity"

	def form_valid(self, form):
		supplier = self.get_account()
		form.instance.supplier = supplier
		valid_data = super(CreateActivityView, self).form_valid(form)
		# form.instance.managers.add(User)
		# add all default users
		return valid_data

	# def get_success_url(self):
	#  	return reverse("product_list_view")


class UpdateActivityView(ProductManagerMixin,SubmitBtnMixin, MultiSlugMixin, UpdateView):
	model = Activity
	template_name = "activities/form.html"
	form_class = ActivityAddForm
	success_url = "/supplier/activities"
	submit_btn = "Update Activity"

class ActivityDetailView(MultiSlugMixin, DetailView):
	model = Activity
	template_name = "activities/detail_view.html"

class SuppliersActivitiesListView(SupplierAccountMixin,ListView):
	model = Activity
	template_name = "supplier/activities_list_view.html"

	def get_queryset(self, *args, **kwargs):
		qs = super(SuppliersActivitiesListView, self).get_queryset(**kwargs)
		qs = qs.filter(supplier=self.get_account())
		query = self.request.GET.get('q')
		if query:
			qs = qs.filter(
				Q(title__icontains=query)|
				Q(description__icontains=query)|
				Q(tagline__icontains=query)
				# Q(supplier__icontains=query)
			).order_by("order")
		return qs


class ActivitiesListView(ListView):
	model = Activity
	template_name = "activities/list_view.html"

	def get_queryset(self, *args, **kwargs):
		qs = super(ActivitiesListView, self).get_queryset(**kwargs)
		query = self.request.GET.get('q')
		if query:
			qs = qs.filter(
				Q(title__icontains=query)|
				Q(description__icontains=query)|
				Q(tagline__icontains=query)
				# Q(supplier__icontains=query)
			).order_by("order")
		return qs


#
# def create_view(request):
# 	form = ProductModelForm(request.POST or None)
# 	if form.is_valid():
# 		print(form.cleaned_data.get("publish"))
# 		instance = form.save(commit=False)
# 		instance.sale_price = instance.price
# 		instance.save()
# 	template = "form.html"
# 	context = {
# 			"form": form,
# 			"submit_btn": "Create Product"
# 		}
# 	return render(request, template, context)
#
#
# def update_view(request, object_id=None):
# 	activity = get_object_or_404(Activity, id=object_id)
# 	form = ActivityAddForm(request.POST or None, instance=activity)
# 	if form.is_valid():
# 		instance = form.save(commit=False)
# 		#instance.sale_price = instance.price
# 		instance.save()
# 	template = "form.html"
# 	context = {
# 		"object": activity,
# 		"form": form,
# 		"submit_btn": "Update Activity"
# 		}
# 	return render(request, template, context)
#
#
#
# def detail_slug_view(request, slug=None):
# 	activity = Activity.objects.get(slug=slug)
# 	try:
# 		activity = get_object_or_404(Activity, slug=slug)
# 	except Activity.MultipleObjectsReturned:
# 		activity = Activity.objects.filter(slug=slug).order_by("-title").first()
# 	# print slug
# 	# product = 1
# 	template = "detail_view.html"
# 	context = {
# 		"object": activity
# 		}
# 	return render(request, template, context)
#
#
# def detail_view(request, object_id=None):
# 	activity = get_object_or_404(Activity, id=object_id)
# 	template = "detail_view.html"
# 	context = {
# 		"object": activity
# 		}
# 	return render(request, template, context)
#
# def list_view(request):
# 	# list of items
# 	print(request)
# 	queryset = Activity.objects.all()
# 	template = "list_view.html"
# 	context = {
# 		"queryset": queryset
# 	}
# 	return render(request, template, context)
